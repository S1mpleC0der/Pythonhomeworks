import requests

API = '6418b539e0697f54de8a3df65ebe9444'

parameters = {
    'appid': API,
    'units': 'metric',
    'lang': 'ru'
}

while True:
    city_name = input('Enter city: ')

    try:
        parameters['q'] = city_name
        response = requests.get('https://api.openweathermap.org/data/2.5/weather',
                                params=parameters).json()

        name = response['name']
        description = response['weather'][0]['description']
        temp = response['main']['temp']
        wind_speed = response['wind']['speed']
        timezone = response['timezone']
        humidity = response['main']['humidity']

        print(f"""The weather is {description} in {name}
Temperature: {temp}
Wind speed: {wind_speed}
Timezone: {timezone}
Humidity: {humidity}""")

    except Exception as e:
        print('Shaxar nomi natogri kiritilgan!', e)