from celery import Celery


app = Celery('app_name', broker='redis://redis_service')

@app.task
def add(x, y):
    return x + y

