import requests
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
hmdt1=str(hmdt)
wind_spd = api_data['wind']['speed']
wind_spd1=str(wind_spd)
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

fileptr = open("weather.txt","a+")
fileptr.write("-------------------------------------------------------------")
fileptr.write("\nWeather Stats for - {} ".format(location.upper()))
fileptr.write(date_time)
fileptr.write("\n-------------------------------------------------------------")
fileptr.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
fileptr.write("\nCurrent weather desc  :")
fileptr.write(weather_desc)
fileptr.write("\nCurrent Humidity      :")
fileptr.write(hmdt1)
fileptr.write("% \nCurrent wind speed    :")
fileptr.write(wind_spd1)
fileptr.write("kmph")
fileptr.close();