from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y



"""
When processing messages, over time our services will fail for some reason such as

The message payload is correct, however the service’s database is down, or some other dependency resource (VM dies), and we need to provide a small delay to allow for the service to become operational again.
The payload is incorrect and it requires for some sort of manual intervention.
The service code is incorrect and an engineer needs to deploy a code fix.
These are some of the reason’s which pop to mind when writing this post at 4am.

Rabbit has support deadletter queues out of the box, which solves 2 and 3 listed above.

However it does not really have an answer for issue 1. (or at least not production ready).


Next step:

- try handling retries of different types of errors

"""
