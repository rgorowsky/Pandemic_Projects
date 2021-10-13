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

search_key = 'ETH'
for x in coin_data: # trying to print the 
  key_key = x['symbol']
  if search_key == key_key:
    print(key_key, x['quote'])

# this prints the data on the top 5 listed coins (assuming details from params section)
# for x in coin_data: 
#   print(x['symbol'], x['quote'])
