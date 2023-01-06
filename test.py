import CryptAPI

ca = CryptAPI.Helper('ltc', 'ltc1qsnpd4qyv9rtejrg2gg36mwax7a72u79rayjlcf',
                     'https://webhook.site/90bf4674-3cf7-4f26-a6d6-cb72bb453aa8', None, {
                        'order_id': 1345
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
print(CryptAPI.Helper.get_info('btc'))

"""
Get all supported coins
"""
print('get_supported_coins:')
print(CryptAPI.Helper.get_supported_coins())

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
