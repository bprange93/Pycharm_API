import requests


def run_api():
    response = requests.get(
        "https://api.yelp.com/v3/businesses/l7mNzyV3pOZ3m87jRY6J7A/reviews")
    print(response.json())
