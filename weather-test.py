#! /usr/bin/python3
# @null-talisman

# imports 
import requests
from pyowm import OWM
from pprint import pprint

API_key = "3b35bed55ea3e8d31402bfa9fdd9aef7"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
owm = OWM('3b35bed55ea3e8d31402bfa9fdd9aef7')
#mgr = owm.weather_manager()

def main():
    # demo 1
    city_name = input("Enter a city Name : ")
    #test_city = owm.three_hours_forecast(city_name)
    #print(test_city.will_have_clouds())
    
    # demo 2
    mgr = owm.weather_manager()
    test_city = owm.weather_at_place(city_name)
    test_weather = test_city.get_weather()
    test_temp = test_weather.get_temperature('fahrenheit')['temp']
    print("\nCurrent Temperature in " + city_name + ": " + str(test_temp) + "*F")
    daily_forecast = mgr.forecast_at_place(city_name, 'daily').forecast
    three_h_forecast = mgr.forecast_at_place(city_name, '3h').forecast
    print(daily_forecast)
    print(three_h_forecast) 

    # demo 3 - different method 
    #Final_url = base_url + "appid=" + API_key + "&q=" + city_name
    #weather_data = requests.get(Final_url).json()
    #print("\nCurrent Weather Data Of " + city_name +":\n")
    #pprint(weather_data)


if __name__ == "__main__":
    main()
