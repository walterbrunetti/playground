from celery import Celery


app = Celery('app_name', broker='amqp://rabbitmq:5672')

@app.task
def add(x, y):
    return x + y

