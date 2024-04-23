"""
CryptAPI's Python Helper
"""

import requests
from requests.models import PreparedRequest


class CryptAPIException(Exception):
    pass


class CryptAPIHelper:
    CRYPTAPI_URL = 'https://api.cryptapi.io/'
    CRYPTAPI_HOST = 'api.cryptapi.io'

    def __init__(self, coin, own_address, callback_url, parameters=None, ca_params=None):
        if not parameters:
            parameters = {}

        if not ca_params:
            ca_params = {}

        if not callback_url:
            raise Exception("Callback URL is Missing")

        if not coin:
            raise Exception('Coin is Missing')

        if not own_address:
            raise Exception('Address is Missing')

        self.coin = coin
        self.own_address = own_address
        self.callback_url = callback_url
        self.parameters = parameters
        self.ca_params = ca_params
        self.payment_Address = ''

    def get_address(self):
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

        if self.parameters:
            req = PreparedRequest()
            req.prepare_url(self.callback_url, self.parameters)
            self.callback_url = req.url

        params = {
            'callback': callback_url
        }

        return CryptAPIHelper.process_request(coin, endpoint='logs', params=params)

    def get_qrcode(self, value='', size=300):
        params = {
            'address': self.payment_Address,
            'size': size
        }

        if value:
            params['value'] = value

        return CryptAPIHelper.process_request(self.coin, endpoint='qrcode', params=params)

    def get_conversion(self, from_coin, value):
        params = {
            'from': from_coin,
            'value': value
        }

        return CryptAPIHelper.process_request(self.coin, endpoint='convert', params=params)

    @staticmethod
    def get_info(coin=''):
        return CryptAPIHelper.process_request(coin, endpoint='info')

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

        return CryptAPIHelper.process_request(coin, endpoint='estimate', params=params)

    @staticmethod
    def process_request(coin=None, endpoint='', params=None):
        if coin:
            coin += '/'
        else:
            coin = ''

        response = requests.get(
            url="{base_url}{coin}{endpoint}/".format(
                base_url=CryptAPIHelper.CRYPTAPI_URL,
                coin=coin.replace('_', '/'),
                endpoint=endpoint,
            ),
            params=params,
            headers={'Host': CryptAPIHelper.CRYPTAPI_HOST},
        )

        response_obj = response.json()

        if response_obj.get('status') == 'error':
            raise CryptAPIException(response_obj['error'])

        return response_obj
