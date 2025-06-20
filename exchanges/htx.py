# exchanges/htx.py
import requests

def get_price_htx(symbol="BTC_USDT"):
    url = f"https://api.huobi.pro/market/detail/merged?symbol={symbol.lower().replace('_', '')}"
    response = requests.get(url)
    data = response.json()["tick"]
    return float(data["ask"][0])
