

# Fun RabbitMQ messaging project

Small project to have fun with Celery, Rabbit and Docker

Where am I?
- Basic setup is done, docker images are working. There is a small task that does something.
  Meseges are produced manually.
- This is the course I'm following: https://app.pluralsight.com/course-player?clipId=5081eeeb-2026-4739-8d15-f0efbaa0c196


Next step:

28/07/2020
- Make sure RabbitMQ setup matches the one on placementLog (specially the auth and credentials)


## Useful links
https://www.fullstackpython.com/celery.html
https://www.rabbitmq.com/getstarted.html
https://www.codeproject.com/Articles/1224515/Python-Celery-RabbitMQ-Tutorial
https://betterprogramming.pub/distributed-task-queues-with-celery-rabbitmq-django-703c7857fc17


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
- check and try concepts like one worker accessing one queue and 2 workers accesing one/multiple queues, etc

"""
