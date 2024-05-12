import requests


def weather_app():

    key = '5ac1a588e2579a6751fede182ff91a5a'

    user_input = input('Enter a city: ')

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={key}")

    if weather_data.json()['cod'] == '404':
        print('The city does not exist! ')
    else :
        weather = weather_data.json()['weather'][0]['main']
        temp = round((weather_data.json()['main']['temp'] - 32)*(5/9))
        print(f'The weather in {user_input} is : {weather} ')
        print(f'The temperature in {user_input} is : {temp}ºC ')


weather_app()