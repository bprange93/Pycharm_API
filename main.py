import requests
from YelpAPI import api_key

API_KEY = api_key()
ENDPOINT = 'https://api.yelp.com/v3/businesses/{id}/reviews'
HEADERS = {'Authorization': 'bearer %s' % api_key}

PARAMETERS = {'id': 'l7mNzyV3pOZ3m87jRY6J7A'}


response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)
print(response.json())
