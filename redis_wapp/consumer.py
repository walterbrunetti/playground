import time
import requests
from celery_app import celery_app


@celery_app.task
def add(x, y):
    requests.get(f"http://www.x.com?q={y}")
    requests.get("http://www.cc.com")
    return x + y

@celery_app.task
def do_something():
    resp = requests.get("http://www.qq.com")
    return resp
