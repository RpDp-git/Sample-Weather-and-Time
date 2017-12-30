import datetime
import requests

def getweather(city):
    appid= "" #your app id
    api="http://api.openweathermap.org/data/2.5/weather?appid="+appid+"&q="
    url = api + city
    json_data = requests.get(url).json()
    return json_data

def clock(clk_inf) : # 1 for time, 2 for date
    now=datetime.datetime.today()
    if clk_inf==1 :
        return print("{:%H:%M}".format(now))
    elif clk_inf==2 :
        return print("{:%A, %b %d}".format(now))
    else :
        return print("Wrong Argument!")

def weather(city, weather_inf) : # weather_inf= 1 for weather, 2 for temperature
    deg_sym = '\xB0'
    json_data=getweather(city)
    temperature = json_data['main']['temp']
    weather=json_data['weather'][0]['main']
    if weather_inf==1:
        return print(weather)
    elif weather_inf==2 :
        return print(str(int(temperature-273.15))+deg_sym)
    else:
        return print("Wrong Argument")

weather("Leipzig",2)

'''
Sample output !
>>>clock(1)
12:52

>>>clock(2)
Saturday, Dec 30

>>>weather("Leipzig",1)
Rain

>>>weather("Leipzig,2")
4°
'''
