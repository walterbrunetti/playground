import requests


def hit_service(x, y):
    requests.get(f"http://www.google.com?q={y}")
    requests.get("http://www.lacapital.com")
    return x + y


def hit_other_service():
    resp = requests.get("http://www.rosario3.com")
    return resp
