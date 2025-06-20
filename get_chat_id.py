import requests

BOT_TOKEN = "7814473717:AAGw4hABPGwjmUOeK5hWqRDMR1wM7mfOZiA"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
response = requests.get(url)
print(response.json())
