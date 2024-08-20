import telebot
import requests
import datetime
from geopy.geocoders import Nominatim
from config import (BOT_TOKEN, STRING_SESSION)


# hava durumu API belirteçlerini tanımlayın 
WEATHER_TOKEN = 'cbfb1c29dba9b33e67dc1aab3abeae8d'
POLLING_TIMEOUT = None
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['weather'])
def send_weather(message):
    # This message will be print when /weather command is given, also it will ask user for the location and call fetch_weather
    location = 'Enter a Location: '
    sent_message = bot.send_message(message.chat.id, location, parse_mode='Markdown')
    bot.register_next_step_handler(sent_message, fetch_info)
    return location


def location_handler(message):
    # Gets the latitude and longitude from the user's location.
    location = message.text
    # Create a geocoder instance
    geolocator = Nominatim(user_agent="my_app")
    print(geolocator)

    try:
        # Get the latitude and longitude
        location_data = geolocator.geocode(location)
        print (location_data)
        latitude = round(location_data.latitude,2)
        longitude = round(location_data.longitude,2)
        # print(latitude, longitude)
        return latitude, longitude
    except (AttributeError):
        print("Location not found.")


def get_weather(latitude,longitude):
    # URL to make API call to OpenWeatherMap API
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}'.format(latitude, longitude, WEATHER_TOKEN)
    response = requests.get(url)
    return response.json()


# Process weather data, format message, and send to user with unit conversion options
def fetch_info(message): 
    '''
    called when the user provides location in response to the '/weather' command.
    uses the 'location_handler' function to get latitude & longitude of the provided location and 'get_weather' function to fetch the weather data
    extracts weather description from API response and sends to user as message.
    '''
    try:
        latitude, longitude = location_handler(message)
        
        weather = get_weather(latitude,longitude)
        data = weather['list']
        data_2 = data[0]

        info = data_2['weather']
        data_3 = info[0]
        main = data_3['main']

        info = data_2['weather']
        data_3 = info[0]
        description = data_3['description'].capitalize()

        dt_txt = data_2['dt_txt']
        dt = datetime.datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        formatted_date_time = dt.strftime('%A, %B %d, %Y %I:%M %p %Z')

        info = data_2['main']
        temp = info['temp']

        info = data_2['main']
        temp_max = info['temp_max']

        info = data_2['main']
        temp_min = info['temp_min']

        info = data_2['wind']
        speed = info['speed']

        
        weather_message = f'*Weather:* {main} - {description}\n\n*Temperature:* {temp:.2f}K\n    *Max Temp:* {temp_max:.2f}K\n    *Min Temp:* {temp_min:.2f}K\n\n*Wind Speed:* {speed}m/s\n\n*Weather info updated on:*\n{formatted_date_time}\n'
        bot.send_message(message.chat.id, 'Here\'s the weather!')
        bot.send_message(message.chat.id, weather_message, parse_mode='Markdown')

    except TypeError:
        bot.send_message(message.chat.id, 'Please enter the valid location')
            
print('Starting bot...')
print('Polling...') 
bot.infinity_polling()
