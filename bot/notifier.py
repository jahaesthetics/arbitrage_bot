# bot/notifier.py
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("✅ Бот запущен. Ожидайте сигналы арбитража.")

async def send_arbitrage_alert(text):
    # Здесь укажем ID чата или список ID позже
    chat_id = os.getenv("ALERT_CHAT_ID")
    if chat_id:
        await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML)

def run_bot():
    executor.start_polling(dp, skip_updates=True)
