
import re
import ssl
import urllib.request
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context


def Time():
    now = datetime.now()
    current_Time = now.strftime("[%H:%M:%S]")
    return current_Time

city = input("Input City: ")
response = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f").read().decode()
logFile = "11_1_logFile.txt"



content = open(logFile, "a", encoding='utf-8')
content.write(Time())

cityPattern = r'(?:name":")([^"]+)'
city = re.findall(cityPattern, response)
city = ''.join(city)
content.write(f"Запрос погоды в городе: {city}")

tempPattern= r'(?:temp":)([^,]+)'
temp1 = re.findall(tempPattern, response)
temp1 = ''.join(temp1)
mainStatePattern = r'(?:description":")([^"]+)'
mainState = re.findall(mainStatePattern, response)
mainState = ''.join(mainState)
content.write(f"\nТемпература: {temp1}\u00b0C, {mainState}")

airHumidityPattern = r'(?:humidity":)([^,}]+)'
airHumidity = re.findall(airHumidityPattern, response)
airHumidity = ''.join(airHumidity)
content.write(f"\nВлажность воздуха: {airHumidity}%")

windSpeedPattern = r'(?:speed":)([^,]+)'
windSpeed = re.findall(windSpeedPattern, response)
windSpeed = ''.join(windSpeed)
content.write(f"\nСкорость ветра: {windSpeed} м/с")

atmospherePressurePattern = r'(?:pressure":)([^,]+)'
atmospherePressure = re.findall(atmospherePressurePattern,
                                    response)
atmospherePressure = ''.join(atmospherePressure)
content.write(f"\nАтмосферное давление: {atmospherePressure} мм рт. ст.")

content.write("\n                   \n")


