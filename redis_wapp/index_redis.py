import redis
from flask import Flask
from producer import produce_messages

app = Flask(__name__)
redis_server = redis.Redis(host='redis', port=6379)


@app.route('/')
def hello():
    produce_messages()
    return 'Messeges were produced\n'


@app.route('/redis')
def redis_status():
    queue_1 = redis_server.llen("pipeline_1")
    queue_2 = redis_server.llen("pipeline_2")
    queue_3 = redis_server.llen("pipeline_3")
    return "Q1 {} - Q2 {} - Q3 {}".format(queue_1, queue_2, queue_3)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
