import time

import redis
from flask import Flask

app = Flask(__name__)
redis_server = redis.Redis(host='redis', port=6379)


from producer import produce_messages


# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)


@app.route('/')
def hello():
    #count = get_hit_count()
    produce_messages()
    return 'Hello World! I have been seen {} times WWW.\n'.format(11)


@app.route('/redis')
def redis_status():
    queue_1 = redis_server.llen("pipeline_1")
    queue_2 = redis_server.llen("pipeline_2")
    return "Q1 {} - Q2 {}".format(queue_1, queue_2)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
