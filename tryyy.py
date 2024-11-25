import requests
import json

class Weather:
    weather ='weatherApi.json'
    
    def __init__(self,api_key):
        self.api_key=api_key
        self.base_url="http://api.weatherapi.com/v1"

    def get_current_temperature(self,city,language):
        url=f"{self.base_url}/current.json?key={self.api_key}&q={city}&lang={language}"
        response=requests.get(url)
        if response.status_code == 200:
            data=response.json()
            self.save(data)
            return data['current']['temp_c']
        else:
            return 

    def get_temperature_after(self,city,days,hour=None):
        url = f"{self.base_url}/forecast.json?key={self.api_key}&q={city}&days={days}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.save(data)
            if hour is None:
                return data['forecast']['forecastday'][days-1]['day']['avgtemp_c']
            else:
                return data['forecast']['forecastday'][days-1]['hour'][hour]['temp_c']
        else:
            return 

    def get_lat_and_long(self, city):
        url = f"{self.base_url}/search.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.save(data)
            if data:
                return data[0]['lat'], data[0]['lon']
        return None

    @classmethod
    def load(cls):
        try:
            with open(cls.weather) as fileobject:
                weather = json.load(fileobject)
        except (FileNotFoundError, json.JSONDecodeError):
            weather=[]
        return weather

    def save(self, data):
        weather = self.load()
        weather.append(data)
        try:
            with open(self.weather, mode='w') as weather_file:
                json.dump(weather, weather_file, indent=4)
            return True
        except Exception as e:
            print(e)
            return False

client = Weather("25b8b73567ad471fadc185314242511")
print(client.get_current_temperature("Kafr Ash Shaykh", "Arabic"))
print(client.get_temperature_after("Kafr Ash Shaykh", 3, 4))
print(client.get_lat_and_long("Kafr Ash Shaykh"))