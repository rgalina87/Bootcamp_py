from pyowm.weatherapi25.observation import Observation
from datetime import date
from pyowm.owm import OWM
import requests
import json
import calendar

owm = OWM('0ad621d7b425b692a4b3725b12b4593d')

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print(f'Today is a {d1}')

city_name = input("Enter city name : \n>>>")
country = input("Enter country : \n>>>")


reg = owm.city_id_registry()
city = reg.ids_for(city_name.title(), country.upper())
city_id = city[0][0]
print(f"Place ID is: {city_id}")
print(f'Weather in {city_name}, {country} is:')

reg = owm.city_id_registry()
coord = reg.locations_for(city_name.title(), country.upper())
loc_coord = coord[0][0]
lat = coord.lat
lon = coord.lon
print(lon, lat)

coi = owm.coindex_around_coords(lat, lon, start=today,    interval="hours")
print(coi)

mgr = owm.weather_manager()
weather = mgr.weather_at_place(city_name.title()).weather
temp_dict_celsius = weather.temperature("celsius")
print(f"The temperature is {temp_dict_celsius} celsius")

wind = weather.wind(unit="miles_hour")
print(f"The wind is {wind}: ")

sunrise = weather.sunrise_time(timeformat='iso')
sunset = weather.sunset_time(timeformat='iso')

print(sunrise)
print(sunset)





