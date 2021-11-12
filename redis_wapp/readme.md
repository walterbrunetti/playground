

# Redis wapp project

Small project to have fun with Celery, Redis and Docker

## How to run it
- docker-compose build
- docker-compose up
- http://localhost:5000/

## Produce a message
docker exec -ti redis_wapp_consumer_1 sh
>>> from consumer import add
>>> add.delay(1,2)
<AsyncResult: 9c60a4f3-fc68-4503-b363-cddd319bd9e5>


## Project status and next steps

App and Containers are working.

Next step: find some representative scenarios from regular apps and replicate.

- Agregar muchos mensages de una y ver que pasa si se agregan mas workers.
- Hay retries?
- rate_limit
- que pasa con los mensajes que hay en la cola si celery esta offline y lo tengo que restartear?
- como agrego a la queue sin llamar directamente al worker?

# Redis commands
redis-cli -h redis_service -p 6379 -n 1 llen celery

## Links I'm following
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
https://www.fullstackpython.com/celery.html

