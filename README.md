[<img src="https://i.imgur.com/IfMAa7E.png" width="300"/>](image.png)


# CryptAPI's Python Library
Python implementation of CryptAPI's payment gateway

## Requirements:

```
Python >= 3.0
Requests >= 2.20
```

## Install

```shell script
pip install python-cryptapi
```

[on pypi](https://pypi.python.org/pypi/python-cryptapi)
or
[on GitHub](https://github.com/cryptapi/python-cryptapi)

## Usage

### Importing in your project file

```python
from cryptapi import CryptAPIHelper
```

### Generating a new Address

```python
from cryptapi import CryptAPIHelper

ca = CryptAPIHelper(coin, myAddress, callbackUrl, params, cryptapiParams)

address = ca.getAddress()['address_in']
```

Where:

* `coin` is the coin you wish to use, from CryptAPI's supported currencies (e.g 'btc', 'eth', 'erc20_usdt', ...).
* `myAddress` is your own crypto address, where your funds will be sent to.
* `callbackUrl` is the URL that will be called upon payment.
* `params` is any parameter you wish to send to identify the payment, such as `{orderId: 1234}`.
* `cryptapiParams` parameters that will be passed to CryptAPI _(check which extra parameters are available here: https://docs.cryptapi.io/#operation/create).
* `address` is the newly generated address, that you will show your users in order to receive payments.

### Getting notified when the user pays

> Once your customer makes a payment, CryptAPI will send a callback to your `callbackUrl`. This callback information is by default in ``GET`` but you can se it to ``POST`` by setting ``post: 1`` in ``cryptapiParams``. The parameters sent by CryptAPI in this callback can be consulted here: https://docs.cryptapi.io/#operation/confirmedcallbackget

### Checking the logs of a request

```python
from cryptapi import CryptAPIHelper

ca = CryptAPIHelper(coin, myAddress, callbackUrl, params, cryptapiParams)

data = ca.get_logs()
```
> Same parameters as before, the ```data``` returned can b e checked here: https://docs.cryptapi.io/#operation/logs

### Generating a QR code

```python
from cryptapi import CryptAPIHelper

ca = CryptAPIHelper(coin, myAddress, callbackUrl, params, cryptapiParams)

###

qr_code = ca.get_qrcode(value, size)
```
For object creation, same parameters as before. You must first call ``getAddress` as this method requires the payment address to have been created.

For QR Code generation:

* ``value`` is the value requested to the user in the coin to which the request was done. **Optional**, can be empty if you don't wish to add the value to the QR Code.
* ``size`` Size of the QR Code image in pixels. Optional, leave empty to use the default size of 512.

> Response is an object with `qr_code` (base64 encoded image data) and `payment_uri` (the value encoded in the QR), see https://docs.cryptapi.io/#operation/qrcode for more information.

### Estimating transaction fees

```python
from cryptapi import CryptAPIHelper

ca = CryptAPIHelper(coin, myAddress, callbackUrl, params, cryptapiParams)

fees = ca.get_estimate(coin, addresses, priority)
```
Where: 
* ``coin`` is the coin you wish to check, from CryptAPI's supported currencies (e.g 'btc', 'eth', 'erc20_usdt', ...)
* ``addresses`` The number of addresses to forward the funds to. Optional, defaults to 1.
* ``priority`` Confirmation priority, (check [this](https://support.cryptapi.io/article/how-the-priority-parameter-works) article to learn more about it). Optional, defaults to ``default``.

> Response is an object with ``estimated_cost`` and ``estimated_cost_usd``, see https://docs.cryptapi.io/#operation/estimate for more information.

### Converting between coins and fiat

```python
from cryptapi import CryptAPIHelper

ca = CryptAPIHelper(coin, myAddress, callbackUrl, params, cryptapiParams)

conversion = ca.get_conversion(value, from_coin)
```
Where:
* ``coin`` the target currency to convert to, from CryptAPI's supported currencies (e.g 'btc', 'eth', 'erc20_usdt', ...)
* ``value`` value to convert in `from`.
* ``from_coin`` currency to convert from, FIAT or crypto.

> Response is an object with ``value_coin`` and ``exchange_rate``, see https://docs.cryptapi.io/#operation/convert for more information.

### Getting supported coins
```python
from cryptapi import CryptAPIHelper

supportedCoins = CryptAPIHelper.get_supported_coins()
```

> Response is an array with all supported coins.

## Help

Need help?  
Contact us @ https://cryptapi.io/contacts/


### Changelog

#### 1.0.0
* Initial Release

#### 1.0.1
* Minor fixes

#### 1.0.2
* Minor fixes

#### 1.0.3
* Minor fixes

#### 1.0.4
* Minor fixes
