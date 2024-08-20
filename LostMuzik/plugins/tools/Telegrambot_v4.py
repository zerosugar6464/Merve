from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.enums import ParseMode
import python_weather

import asyncio
import datetime
import os
import math

from settings import *


# Weather
# p_weather_Bot


dp = Dispatcher()
router = Router(name=__name__)


async def getweather(city: str, is_forecast: bool = True):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC, locale=python_weather.Locale.RUSSIAN) as client:
        # fetch a weather forecast from a cityn
        weather = await client.get(city)

        # returns the current day's forecast temperature (int)
        print(
            f"Current. t: {weather.current.temperature}, wind: {weather.current.description}, precipitation: {weather.current.precipitation}\n")
        res = {"current": weather.current}

        # get the weather forecast for a few days
        print("Forecast.")
        if not is_forecast:
            return res
        res["forecast"] = {}
        for forecast in weather.forecasts:
            print(f"{forecast.date} t: {forecast.temperature}")
            res["forecast"][str(forecast.date)] = {"temperature": forecast.temperature, "unit": forecast.unit,
                                                   "lowest_temperature": forecast.lowest_temperature,
                                                   "highest_temperature": forecast.highest_temperature,
                                                   "astronomy": forecast.astronomy,
                                                   "snowfall": forecast.snowfall, "sunlight": forecast.sunlight}

            # hourly forecasts
            for hourly in forecast.hourly:
                if hourly.time == datetime.time(9, 0):
                    res["forecast"][str(forecast.date)]["morning"] = hourly
                    print(
                        f"  Morning --> t: {hourly.temperature}, precipitation: {hourly.precipitation}, {hourly.description.lower()}")
                if hourly.time == datetime.time(15, 0):
                    res["forecast"][str(forecast.date)]["day"] = hourly
                    print(
                        f"  Day     --> t: {hourly.temperature}, precipitation: {hourly.precipitation}, {hourly.description.lower()}")
                if hourly.time == datetime.time(21, 0):
                    res["forecast"][str(forecast.date)]["evening"] = hourly
                    print(
                        f"  Evening --> t: {hourly.temperature}, precipitation: {hourly.precipitation}, {hourly.description.lower()}")
        return res


@dp.message(Command("weather"))
async def cmd_weather(message: types.Message, command: CommandObject):
    print("/weather")

    city = command.args
    if city is None:
        return await message.reply("Кажется вы забыли указать название города.")
    try:
        weather = await getweather(city, False)
    except:
        return await message.reply("Во время обработки вашего запросы произошла ошибка. Попробуйте ещё раз.")
    print(weather)

    answer = (f"В городе {city} сейчас {weather['current'].description.lower().replace('дымка', 'туман').replace('снежный ливень', 'дождь со снегом')}, "
              f"температура воздуха: {weather['current'].temperature}°C, "
              f"ощущается как {weather['current'].feels_like}°C, влажность: "
              f"{weather['current'].humidity}%, скорость ветра: "
              f"{math.floor(weather['current'].wind_speed * 0.27778)} м/с, ")

    await message.reply(answer)

@dp.message(Command("forecast"))
async def cmd_forecast(message: types.Message, command: CommandObject):
    print("/forecast")

    city = command.args
    if city is None:
        return await message.reply("Кажется вы забыли указать название города.")
    try:
        forecast = await getweather(city, True)
        forecast = forecast["forecast"]
    except:
        return await message.reply("Во время обработки вашего запросы произошла ошибка. Попробуйте ещё раз.")
    print(forecast)

    answer = f"Прогноз погоды на 3 дня для города {city}:\n\n"
    for date, weather in forecast.items():
        t = ""
        if str(datetime.date.today()) == date:
            t = " (сегодня)"
        elif str(datetime.date.today() + datetime.timedelta(days=1)) == date:
            t = " (завтра)"
        answer += f"""Прогноз погоды на {date}{t}:
   Утром {weather['morning'].description.lower().replace('дымка', 'туман').replace('снежный ливень', 'дождь со снегом')},
    температура воздуха: {weather['morning'].temperature}°C,
    вероятность выпадения осадков: {max(weather['morning'].chances_of_rain, weather['morning'].chances_of_snow)}%
   Днём {weather['day'].description.lower().replace('дымка', 'туман').replace('снежный ливень', 'дождь со снегом')},
    температура воздуха: {weather['day'].temperature}°C,
    вероятность выпадения осадков: {max(weather['day'].chances_of_rain, weather['day'].chances_of_snow)}%
   Вечером {weather['evening'].description.lower().replace('дымка', 'туман').replace('снежный ливень', 'дождь со снегом')},
    температура воздуха: {weather['evening'].temperature}°C,
    вероятность выпадения осадков: {max(weather['evening'].chances_of_rain, weather['evening'].chances_of_snow)}%\n\n"""
        print(date, weather)

    await message.reply(answer)

@dp.message(Command("code"))
async def cmd_help(message: types.Message):
    print("/code")
    await message.reply("Исходны код бота доступен на Github: https://github.com/AlexK-1/Weather-telegram-bot")

async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
