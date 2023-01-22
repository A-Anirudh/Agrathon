from django.core.exceptions import ObjectDoesNotExist
import requests
from geopy.distance import geodesic
from .models import Customer, Farmer
def get_lat_and_lon(username,user_type="consumer"):
    try:
        if user_type == "consumer":
            city = Customer.objects.get(name=username).city
        else:
            city = Farmer.objects.get(name=username).city

        url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=c0a19e7a5f55b085ab99c23b15604505"

        result = requests.get(url)
        lat = (result.json()[0]['lat'])
        lon = (result.json()[0]['lon'])
        return lat, lon

    except ObjectDoesNotExist:
        print("User not found")
        return -1
