import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

from consumer import add

def produce_messages():
    for x in range(100):
        add.delay(1,x)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    #count = get_hit_count()
    produce_messages()
    return 'Hello World! I have been seen {} times WWW.\n'.format(11)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
