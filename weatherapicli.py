import requests
import argparse
import json
parser=argparse.ArgumentParser(description="weather cli")
parser.add_argument("--city",type=str)
args=parser.parse_args()
def getWeather(city):
    api_key="my_api_key"
    url=f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response=requests.get(url)
    data=response.json()
    #print(json.dumps(data,indent=4))
    print("=========")
    print("\nWEATHER REPORT\n")
    print(f"place:{data['location']['name']},{data['location']['country']}")
    print(f"temperature:{data['current']['temp_c']}°C/{data['current']['temp_f']}°F")
    print(f"condition: {data['current']['condition']['text']}")
    print(f"feels like: {data['current']['feelslike_c']}°C/{data['current']['feelslike_f']}°F\n")
    print("=========")

getWeather(args.city)

"""
input:python main.py --city mumbai
output:

=========

WEATHER REPORT

place:Mumbai,India
temperature:33.3°C/91.9°F
condition: Mist
feels like: 40.8°C/105.3°F

=========

"""
