import asyncio
import os
import logging

from telebot.async_telebot import AsyncTeleBot, types

bot = AsyncTeleBot(os.environ.get("BOT_TOKEN"))
logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    text = "Бот запущен"
    await bot.reply_to(message, text)

    logging.info(f"[INFO] Start by {message.from_user.username} | {message.from_user.id}")


if __name__ == "__main__":
    asyncio.run(bot.polling())
