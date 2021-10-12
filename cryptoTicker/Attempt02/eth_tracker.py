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

print(returned_json)
