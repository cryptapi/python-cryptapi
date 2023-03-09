from cryptapi import CryptAPIHelper


ca = CryptAPIHelper('bep20_usdt', '0xA6B78B56ee062185E405a1DDDD18cE8fcBC4395d',
                     'https://webhook.site/15d94bb3-c3ae-4b68-8120-5dd962988a6d', {
                         'order_id': '1345e13232'
                     }, {
                         'convert': 1
                     })

"""
Get CA Address
"""
print('get_address:')
address = ca.get_address()['address_in']
print(address)

"""
Get coin information
"""
print('get_info:')
print(CryptAPIHelper.get_info('btc'))

"""
Get all supported coins
"""
print('get_supported_coins:')
print(CryptAPIHelper.get_supported_coins())

"""
Get Logs
"""
print('get_logs')
print(ca.get_logs())

"""
Get QR Code
"""
print(ca.get_qrcode()['qr_code'])

"""
Get Conversion
"""
print(ca.get_conversion('eur', 100))

"""
Get Estimate
"""
print(ca.get_estimate('ltc'))
