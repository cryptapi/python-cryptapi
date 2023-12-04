"""
CryptAPI's Python Helper
"""

import requests
from requests.models import PreparedRequest

class CryptAPIHelper:
    CRYPTAPI_URL = 'https://api.cryptapi.io/'
    CRYPTAPI_HOST = 'api.cryptapi.io'

    def __init__(self, coin, own_address, callback_url, parameters=None, ca_params=None):
        if parameters is None:
            parameters = {}

        if ca_params is None:
            ca_params = {}

        self.coin = coin
        self.own_address = own_address
        self.callback_url = callback_url
        self.parameters = parameters
        self.ca_params = ca_params
        self.payment_Address = ''

    def get_address(self):
        if self.coin is None or self.own_address is None:
            return None

        coin = self.coin

        if self.parameters:
            req = PreparedRequest()
            req.prepare_url(self.callback_url, self.parameters)
            self.callback_url = req.url

        params = {
            'address': self.own_address,
            'callback': self.callback_url,
            **self.parameters, **self.ca_params}

        _address = CryptAPIHelper.process_request(coin, endpoint='create', params=params)
        if _address:
            self.payment_Address = _address['address_in']
            return _address

        return None

    def get_logs(self):
        coin = self.coin
        callback_url = self.callback_url

        if coin is None or callback_url is None:
            return None

        if self.parameters:
            req = PreparedRequest()
            req.prepare_url(self.callback_url, self.parameters)
            self.callback_url = req.url

        params = {
            'callback': callback_url
        }

        _logs = CryptAPIHelper.process_request(coin, endpoint='logs', params=params)

        if _logs:
            return _logs

        return None

    def get_qrcode(self, value='', size=300):
        if self.coin is None:
            return None

        params = {
            'address': self.payment_Address,
            'size': size
        }

        if value:
            params['value'] = value

        _qrcode = CryptAPIHelper.process_request(self.coin, endpoint='qrcode', params=params)

        if _qrcode:
            return _qrcode

        return None

    def get_conversion(self, from_coin, value):
        params = {
            'from': from_coin,
            'value': value
        }

        _value = CryptAPIHelper.process_request(self.coin, endpoint='convert', params=params)

        if _value:
            return _value

        return None

    @staticmethod
    def get_info(coin=''):
        _info = CryptAPIHelper.process_request(coin, endpoint='info')

        if _info:
            return _info

        return None

    @staticmethod
    def get_supported_coins():
        _info = CryptAPIHelper.get_info('')

        _info.pop('fee_tiers', None)

        _coins = {}

        for ticker, coin_info in _info.items():

            if 'coin' in coin_info.keys():
                _coins[ticker] = coin_info['coin']
            else:
                for token, token_info in coin_info.items():
                    _coins[ticker + '_' + token] = token_info['coin'] + ' (' + ticker.upper() + ')'

        return _coins

    @staticmethod
    def get_estimate(coin, addresses=1, priority='default'):
        params = {
            'addresses': addresses,
            'priority': priority
        }

        _estimate = CryptAPIHelper.process_request(coin, endpoint='estimate', params=params)

        if _estimate:
            return _estimate

        return None

    @staticmethod
    def process_request(coin='', endpoint='', params=None):
        if coin != '':
            coin += '/'

        response = requests.get(
            url="{base_url}{coin}{endpoint}/".format(
                base_url=CryptAPIHelper.CRYPTAPI_URL,
                coin=coin.replace('_', '/'),
                endpoint=endpoint,
            ),
            params=params,
            headers={'Host': CryptAPIHelper.CRYPTAPI_HOST},
        )

        return response.json()
