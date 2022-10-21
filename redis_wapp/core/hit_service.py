import requests


def hit_service(x, y):
    requests.get(f"http://www.google.com?q={y}")
    requests.get("https://www.reddit.com/r/Wallstreetbets/top.json?limit=10&t=year")  # Reddit public content
    return x + y


def hit_other_service():
    resp = requests.get("https://open.er-api.com/v6/latest/USD")  # USD Exchange rates
    return resp

def hit_extra_service():
    resp = requests.get("https://api2.binance.com/api/v3/ticker/24hr")  # Binance 24 hr crypto data
    return resp
