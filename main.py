import requests
from YelpAPI import api_key

API_KEY = "X9N5k658alNxj9wvD0l5IFtG7If-WIUDA7R_x06BVGzAc0pQ7IvvIV15Hurp6gIfzubjHD-6W69Yf8oEVj8pH5V49t1ctBwvAHox4cPw2f" \
          "5N738Ku1CLlBW4Moo7YXYx"
ENDPOINT = 'https://api.yelp.com/v3/businesses/l7mNzyV3pOZ3m87jRY6J7A/reviews'
HEADERS = {'Authorization': 'bearer %s' % api_key}


response = requests.get(url=ENDPOINT, headers=HEADERS)
reviews = response.json()
print(reviews['list'])
