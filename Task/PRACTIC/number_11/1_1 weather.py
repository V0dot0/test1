
import re
import ssl
import urllib.request

from datetime import datetime
def Time():
    now = datetime.now()
    current_Time = now.strftime("[%H:%M:%S]")
    return current_Time


ssl._create_default_https_context = ssl._create_unverified_context
inputCity = input("Input City: ")
url= ("https://api.openweathermap.org/data/2.5/weather?q=" + inputCity
      + "&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f")
response= urllib.request.urlopen(url).read().decode()
logFile = "logFile.txt"


def requestLog(requestedFile, requestedData):
    content = open(requestedFile, "a", encoding='utf-8')
    content.write(Time())

    cityPattern = r"(\"name\"\:\")([^\"}]*)"
    city = re.findall(cityPattern, requestedData)
    city = ''.join(city)
    content.write(f" Запрос погоды в городе: {city}")

    tempPattern= r"(?:\"temp\"\:)([^\.]*)"
    temp = re.findall(tempPattern, requestedData)
    temp = ''.join(temp)
    mainStatePattern = r"(?:\,\"description\"\:\")([^\"]*)"
    mainState = re.findall(mainStatePattern, requestedData)
    mainState = ''.join(mainState)
    content.write(f"\nТемпература: {temp}\u00b0C, {mainState}")

    airHumidityPattern = r"(?:\"humidity\"\:)([^\D]*)"
    airHumidity = re.findall(airHumidityPattern, requestedData)
    airHumidity = ''.join(airHumidity)
    content.write(f"\nВлажность воздуха: {airHumidity}%")

    windSpeedPattern = r"(?:\"speed\"\:)([^\D}]*)"
    windSpeed = re.findall(windSpeedPattern, requestedData)
    windSpeed = ''.join(windSpeed)
    content.write(f"\nСкорость ветра: {windSpeed} м/с")

    atmospherePressurePattern = r"(?:\"pressure\"\:)([^\D}]*)"
    atmospherePressure = re.findall(atmospherePressurePattern,
                                          requestedData)
    atmospherePressure = ''.join(atmospherePressure)
    content.write(f"\nАтмосферное давление: {atmospherePressure} мм рт. ст.")

    content.write("\n                   \n")
    content.close()


requestLog(logFile, response)