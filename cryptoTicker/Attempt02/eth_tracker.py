import apikey
import requests

# The header object is a 'dictionary'
headers = {
  'X-CMC_PRO_API_KEY' : apikey.key,
  'Accepts' : 'Application/json'
}

# The params object is a 'dictionary'
params = {
  "start" : '1',
  'limit' : '5',
  'convert' : 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

returned_json = requests.get(url, params=params, headers=headers).json()

coin_data = returned_json['data']

# for printing etherum prices
eth_search_key = 'ETH'
for x in coin_data:
  eth_abbrev = x['symbol']
  eth_price = x['quote']['USD']['price']
  if eth_search_key == eth_abbrev:
    print(eth_abbrev, eth_price)

# for printing bitcoin prices
btc_search_key = 'BTC'
for x in coin_data:
  btc_abbrev = x['symbol']
  btc_price = x['quote']['USD']['price']
  if btc_search_key == btc_abbrev:
    print(btc_abbrev, btc_price)

# for printing binance coin prices
bnb_search_key = 'BTC'
for x in coin_data:
  bnb_abbrev = x['symbol']
  bnb_price = x['quote']['USD']['price']
  if bnb_search_key == bnb_abbrev:
    print(bnb_abbrev, bnb_price)

# for printing cardano coin prices
ada_search_key = 'ADA'
for x in coin_data:
  ada_abbrev = x['symbol']
  ada_price = x['quote']['USD']['price']
  if ada_search_key == ada_abbrev:
    print(ada_abbrev, ada_price)

# print all 5 coins
# for x in coin_data:
#   print(x['symbol'], x['quote']['USD']['price'])
