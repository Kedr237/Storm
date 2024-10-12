import asyncio
import logging
import os

from telebot.async_telebot import AsyncTeleBot, types

from helpers import messages, requests

bot = AsyncTeleBot(os.environ.get("BOT_TOKEN"))
logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await bot.reply_to(message, messages.start)
    logging.info(f"Start by {message.from_user.username} | {message.from_user.id}.")


@bot.message_handler(func=lambda message: True)
async def send_weather(message: types.Message):
    city_info = await requests.get_city_info(message.text)
    if city_info:
        response_message = messages.weather_info % (
            city_info["location"]["name"],
            city_info["current"]["condition"]["text"],
            city_info["current"]["temp_c"],
            city_info["location"]["localtime"]
        )
        await bot.reply_to(message, response_message)
    else:
        await bot.reply_to(message, messages.unknown_city)
    logging.info(f"{message.from_user.username} searched for '{message.text}'.")


if __name__ == "__main__":
    asyncio.run(bot.polling())
