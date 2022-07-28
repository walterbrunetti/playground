# Redis wapp project

Small project to have fun with Celery, Redis and Docker

## How to run it
- docker-compose build && docker-compose up
- http://localhost:5000/
- http://localhost:5555/  # flower: working but not showing queues
- http://localhost:5000/redis  # workaround to see queues number of messages

## Produce a message
docker exec -ti redis_wapp_consumer_1 sh
>>> from consumer import add
>>> add.delay(1,2)
<AsyncResult: 9c60a4f3-fc68-4503-b363-cddd319bd9e5>


## Project status and next steps

Status:
- App and Containers are working.
- Flower is showing workers but not queues for some reason.
- there's an endpoint that produces 50 messages.
- there's only one consumer (worker) that consume from 2 queues
- worker does 2 tasks. Each task goes to different queues

Next steps:
- 2 workers for one queue, 4 for another (Say you have two servers, x, and y that handle regular tasks, and one server z, that only handles feed related tasks)
  * https://docs.celeryq.dev/en/latest/userguide/routing.html
- Add a bunch of messages at once and see how it behaves when adding more workers.
  * Use fixed number of workers (vs autoscaling)
- rate_limit
- what about retries?
- Dependencies between tasks: Chains - groups - chords
- how adding messages to a queue without calling the producer directly?
    * https://flower.readthedocs.io/en/latest/api.html
    * post a message from redis directly?
    * celery.send_task('job1', args=[], kwargs={}, queue='queue_name_1')
      celery.send_task('job1', args=[], kwargs={}, queue='queue_name_2')
- a tasks hangs. What happenes? should we restart the worker? what happenes with the messege that was processing and other messagses
- Ofair (main process only send task to child when it's available)
  - prefetch_multiplier = 1   # what is celery prefetching?
    prefetch_multiplier=1 (main process will not take more task than it needs - 1 per child)
- monitoring celery/tasks (flower - new rellic/data dog/ graphite-grafana/logentries)
  * https://flower.readthedocs.io/en/latest/prometheus-integration.html#start-grafana







# Redis commands
redis-cli -h redis_service -p 6379 -n 1 llen celery


## Links I'm following
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
https://www.fullstackpython.com/celery.html
https://www.vinta.com.br/blog/2017/celery-overview-archtecture-and-how-it-works/
https://medium.com/analytics-vidhya/python-celery-explained-for-beginners-to-professionals-part-3-workers-pool-and-concurrency-ef0522e89ac5  --> good at explaining concepts


## Notes
* Celery got a master process. Workers are Childs.
* Concepts:
  - task is a function that does something (cooking)
  - worker (Cooker) is a program that execute tasks
  - A Task Queue is queue of tasks to be executed by workers (the order)
* if the child process dies, celery automatically creates a new one. If master process dies, you can restart it with supervisord


## Idea: Build a program with following features
  - There's a celerybeat that runs every X minutes.
  - It hits an endpoint that get records info (it could get just the ID)
  - If you get just the ID, you add it to a new queue
  - One task reads the ID from the message and hits a new endpoint to get the entire record and save it.
  - If the message contains the entire record (instead of just the record ID), then it just saves it.
  - Is it better to do it in 2 steps? (first get the ID, then the rest, then save)
  - What would happen if the API return a bunch of records, should we implement batch?
  - Let's suppose the record needs some processing before saving. Should we do it in deferent steps (tasks)? task 1 process 1 --> task 2 process 2 --> etc
