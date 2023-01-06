"""
CryptAPI's Python Helper
"""

import requests


class Helper:
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

    def get_address(self):
        if self.coin is None or self.own_address is None:
            return None

        coin = self.coin
        params = {
            'address': self.own_address,
            'callback': self.callback_url,
            **self.parameters, **self.ca_params}

        _address = Helper.process_request(coin, endpoint='create', params=params)
        if _address:
            return _address

        return None

    def get_logs(self):
        coin = self.coin
        callback_url = self.callback_url

        if coin is None or callback_url is None:
            return None

        params = {
            'callback': callback_url
        }

        _logs = Helper.process_request(coin, endpoint='logs', params=params)

        if _logs:
            return _logs

        return None

    def get_qrcode(self, value='', size=300):
        if self.coin is None:
            return None

        params = {
            'address': self.own_address,
            'size': size
        }

        if value:
            params = {
                'address': self.own_address,
                'size': size,
                'value': value
            }

        _qrcode = Helper.process_request(self.coin, endpoint='qrcode', params=params)

        if _qrcode:
            return _qrcode

        return None

    def get_conversion(self, from_coin, value):
        params = {
            'from': from_coin,
            'value': value
        }

        _value = Helper.process_request(self.coin, endpoint='convert', params=params)

        if _value:
            return _value

        return None

    @staticmethod
    def get_info(coin=''):
        _info = Helper.process_request(coin, endpoint='info')

        if _info:
            return _info

        return None

    @staticmethod
    def get_supported_coins():
        _info = Helper.get_info('')

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

        _estimate = Helper.process_request(coin, endpoint='estimate', params=params)

        if _estimate:
            return _estimate

        return None

    @staticmethod
    def process_request(coin='', endpoint='', params=None):
        if coin != '':
            coin += '/'

        response = requests.get(
            url="{base_url}{coin}{endpoint}/".format(
                base_url=Helper.CRYPTAPI_URL,
                coin=coin.replace('_', '/'),
                endpoint=endpoint,
            ),
            params=params,
            headers={'Host': Helper.CRYPTAPI_HOST},
        )

        return response.json()