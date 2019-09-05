from os import environ
from requests import get

_geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address=!&key={environ["GOOGLE_GEOCODING_API_KEY"]}'

geocode = lambda address: get(_geocoding_url.replace('!', address)).json()['results'][0]['geometry']['location']