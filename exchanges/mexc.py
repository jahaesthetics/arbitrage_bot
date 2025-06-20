# exchanges/mexc.py
import requests

def get_price_mexc(symbol="BTC_USDT"):
    url = f"https://api.mexc.com/api/v3/ticker/price?symbol={symbol.replace('_', '')}"
    response = requests.get(url)
    return float(response.json()["price"])
