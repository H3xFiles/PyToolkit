from time import sleep

import requests
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")
APIKEY = "c5a92b2f3a9835731d5a3ffd567c7524"
city = ["London,uk","Berlin,de","Amsterdam,nl"]
def QueryCity(CityName):
    APICALL = "http://api.openweathermap.org/data/2.5/weather?q="+CityName+"&appid="+str(APIKEY)
    #print(APICALL)
    data = requests.get(url=APICALL)
    json_bulk = data.json()
    wind = json_bulk["wind"]
    weather = json_bulk["weather"]
    temp = json_bulk["main"]["temp"] - 273.15
    humidity = json_bulk["main"]["humidity"]
    latitude = str(json_bulk["coord"]["lat"])
    longitude = str(int(json_bulk["coord"]["lon"]))
    print("Lat %s- Lon %s " %(latitude, longitude))
    print("Temperature: %i \nHumidity: %i\n" %(temp,humidity,))

for x in city:
    print("\n"+ x)
    print(today)
    QueryCity(x)
    sleep(1)
