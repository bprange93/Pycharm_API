import requests

# key couldn't be pulled from YelpAPI class so was hard coded into this class and YelpAPI class deleted
API_KEY = "X9N5k658alNxj9wvD0l5IFtG7If-WIUDA7R_x06BVGzAc0pQ7IvvIV15Hurp6gIfzubjHD-6W69Yf8oEVj8pH5V49t1ctBwvAHox4cPw2f" \
          "5N738Ku1CLlBW4Moo7YXYx"
# this is the API call in order to get the information for La Cabana
#this API only puts out 3 reviews per restaurant
#parameter for this API is built into the call 'l7mNzyV3pOZ3m87jRY6J7A' is the id which is the parameter
ENDPOINT = 'https://api.yelp.com/v3/businesses/l7mNzyV3pOZ3m87jRY6J7A/reviews'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

response = requests.get(url=ENDPOINT, headers=HEADERS)
# turned response into reviews to show exactly what I am trying to display
reviews = response.json()
print(reviews)

