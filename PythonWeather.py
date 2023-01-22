# ============================ INFORMATION =============================
#
# About: Simple terminal-interface weather program which utilizes
#        custom built temperature/weather color readouts based on
#        conditions. Built off the python_weather API.
#
# ======================== IMPORT STATEMENTS ==========================

import python_weather
import asyncio
import os
import time
import colors as cc

# =========================== WEATHER FUNCTION ==========================

def clearer():
    os.system('cls' if os.name == 'nt' else 'clear')

def marker():
    print("\n>>  ",end='')

def getCity(city):
    clearer()
    marker()
    if city == 'Unknown\n' or city == "Unknown":
        newcity = input("What city would you like to look at?: ")
        weatherLoader(newcity)
        return newcity
    weatherLoader(city)
    return city

def tempColor(temp):
    color = ''
    if temp <= -20:
        color = "Extremecold"
    elif -20 < temp <= 0:
        color = "Freezing"
    elif 0 < temp <= 10:
        color = "Cold"
    elif 10 < temp <= 20:
        color = "Chilly"
    elif 20 < temp <= 40:
        color = "Moderate"
    elif 40 < temp <= 50:
        color = "Normal"
    elif 50 < temp <= 60:
        color = "Temperate"
    elif 60 < temp <= 70:
        color = "Warm"
    elif 70 < temp <= 80:
        color = "Verywarm"
    elif 80 < temp <= 90:
        color = "Hot"
    elif temp >= 90:
        color = "Veryhot"
    return color

def weatherPrint(weather, city):
    head = "+------------------------------------------------------------------------------+"
    print(head)
    text = "CRINGE WEATHER"
    print(f"|{text:^78}|")
    print(head)
    header = f"Current Temperature in {city} --> "
    current_temp = weather.current.temperature
    headcolor = tempColor(current_temp)
    #print(len(cc.cringe(current_temp, color=color)))
    print(f"|{header + cc.cringe(current_temp, color=headcolor):^92}|")
    print(head)
    for forecast in weather.forecasts:
        # hourly forecasts
        for i, hourly in enumerate(forecast.hourly):
            if i == 0:
                print(f"|   DATE: {str(forecast.date)}           SUNRISE: {str(forecast.astronomy.sun_rise)}            SUNSET: {str(forecast.astronomy.sun_set)}   |")
                print(head)
            else:
                hour_temp = str(hourly.temperature)
                nextTempColor = tempColor(int(hour_temp))
                print(f"| {str(hourly.time.hour):^25} {cc.cringe(hour_temp, color=nextTempColor).strip():^36}{cc.cringe(str(hourly.description), color=str(hourly.description)).strip():^39}{'|':^10}")

        print(head)

async def getWeather(city):
    async with python_weather.Client(format="F") as client:
        weather = await client.get(city)
        print()
        # get the weather forecast for a few days
        weatherPrint(weather, city)

def weatherLoader(city):
    marker()
    print(f"LOADING WEATHER DATA FOR --> [{city}]\n")
    bar = [
        " [=     ]",
        " [ =    ]",
        " [  =   ]",
        " [   =  ]",
        " [    = ]",
        " [     =]",
        " [    = ]",
        " [   =  ]",
        " [  =   ]",
        " [ =    ]",
    ]
    i = 0

    while i < 21:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.1)
        i += 1
    clearer()

def main(location = "Unknown"):
    while True:
        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        city = getCity(location)
        asyncio.run(getWeather(city))

if __name__ == "__main__":
    main()
    
