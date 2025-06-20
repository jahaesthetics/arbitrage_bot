import asyncio
from exchanges.htx import get_price_htx
from exchanges.mexc import get_price_mexc
from aiogram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("ALERT_CHAT_ID")

async def send_alert(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(CHAT_ID, message)
    await bot.session.close()

if __name__ == "__main__":
    symbol = "BTC_USDT"
    price_mexc = get_price_mexc(symbol)
    price_htx = get_price_htx(symbol)

    diff = price_htx - price_mexc
    percent = (diff / price_mexc) * 100

    message = (
        f"📊 <b>Анализ {symbol}</b>\n"
        f"MEXC: <code>{price_mexc}</code>\n"
        f"HTX: <code>{price_htx}</code>\n"
        f"💰 Разница: <b>{diff:.2f} USDT</b> ({percent:.2f}%)\n"
    )

    if percent > 1.5:
        message += "✅ <b>Профит найден! Можно арбитражить</b>"
    else:
        message += "❌ Профит < 1.5% — невыгодно"

    print(message)
    asyncio.run(send_alert(message))
