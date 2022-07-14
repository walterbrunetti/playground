FROM python:alpine3.8

RUN pip install celery==5.0.5 redis flask==2.0.1 requests

WORKDIR /app

COPY . .

EXPOSE 5000

CMD python ./index_redis.py
