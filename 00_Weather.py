import requests
import os
from datetime import datetime

# user_api = os.environ['Current Weather Data']
location = input("\n\nEnter your city: ")
api_key = "a3318cc20474c79c538c38eba493aac2"
complete_api_link =f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}"

api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

if api_data['cod']=='404':
    print("Invalid City")
else:
    temp_city = ((api_data['main']['temp'])-273.15)    
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime('%d %b %Y | %I : %M : %S : %p')

    print("------------------------------------------------------")
    print(f"Weather States for - {location.upper()} || {date_time}")
    print("-------------------------------------------------------")

    print("Current tempture is {:.2f} deg C".format(temp_city))
    print("Current weather desc :", weather_desc)
    print(f"Current Humidity : {hmdt}%")
    print(f"Current Wind Speed : {wind_spd}kmph")
