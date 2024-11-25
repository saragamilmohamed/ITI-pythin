import requests

class Weather:
    def __init__(self,api_key):
        self.api_key =api_key
        self.base_url ="http://api.weatherapi.com/v1"

    def get_current_temperature(self,city,language):
        url=f"{self.base_url}/current.json?key={self.api_key}&q={city}&lang={language}"
        response=requests.get(url)
        data=response.json()
        return data['current']['temp_c']

    def get_temperature_after(self,city,days,hour=None):
        
        url=f"{self.base_url}/forecast.json?key={self.api_key}&q={city}&days={days}"
        response=requests.get(url)
        data=response.json()
        
       
        if hour==None:
            return data['forecast']['forecastday'][days-1]['day']['avgtemp_c']
        else:
            return data['forecast']['forecastday'][days-1]['hour'][hour]['temp_c']

    def get_lat_and_long(self,city):
        url=f"{self.base_url}/search.json?key={self.api_key}&q={city}"
        response=requests.get(url)
        data=response.json()
        
        if data:
            return data[0]['lat'], data[0]['lon']



client = Weather("25b8b73567ad471fadc185314242511")
print(client.get_current_temperature("Kafr Ash Shaykh","Arabic"))
print(client.get_temperature_after("Kafr Ash Shaykh", 3,4))
print(client.get_lat_and_long("Kafr Ash Shaykh"))

'''import json
import requests
base_url ="http://api.weatherapi.com/v1"
api_key ="25b8b73567ad471fadc185314242511"
city="Kafr Ash Shaykh"

url=f"{base_url}/current.json?key={api_key}&q={city}"
response=requests.get(url)
data=response.json()
print(data)

import json
import requests
base_url ="http://api.weatherapi.com/v1"
api_key ="25b8b73567ad471fadc185314242511"
city="Kafr Ash Shaykh"
days=3
hour=None
url=f"{base_url}/forecast.json?key={api_key}&q={city}&days={days}&hour={hour}"
response=requests.get(url)
data=response.json()
print(data)'''

