# Redis wapp project

Small project to have fun with Celery, Redis and Docker

## How to run it
- docker-compose build && docker-compose up
- http://localhost:5000/
- http://localhost:5555/  # flower: working but not showing queues
- http://localhost:5000/redis  # workaround to see queues number of messages

## Produce a message
docker exec -ti redis_wapp_consumer_1 sh
```
>>> from consumer import add
>>> add.delay(1,2)
<AsyncResult: 9c60a4f3-fc68-4503-b363-cddd319bd9e5>
```

## Project status and next steps

Status:
- App and Containers are working.
- Flower is showing workers but not queues for some reason.
- there's an endpoint that produces 50 messages.
- there are 3 tasks and one queue for each (so 3 queues)
- there are 2 consumers (workers). One consume from queue 1 and 2. The other from queue 3.

Next steps:
- Use base for tasks - add logging and monitoring on it
- multiple tasks in a single queue
- Add a bunch of messages at once and see how it behaves when adding more workers.
  * Use fixed number of workers (vs autoscaling)  -- does it refer to concurrency?
- rate_limit
- Dependencies between tasks: Chains - groups - chords
- different ways of invoking tasks (delay, apply_async, .s(), etc)
- how adding messages to a queue without calling the producer directly?
    * https://flower.readthedocs.io/en/latest/api.html
    * post a message from redis directly?
    * celery.send_task('job1', args=[], kwargs={}, queue='queue_name_1')
      celery.send_task('job1', args=[], kwargs={}, queue='queue_name_2')
- a tasks hangs. What happens? should we restart the worker? what happenes with the messege that was processing and other messagses
- monitoring celery/tasks (flower - new rellic/data dog/ graphite-grafana/logentries)
  * https://flower.readthedocs.io/en/latest/prometheus-integration.html#start-grafana
- supervisord


# Redis commands
redis-cli -h redis_service -p 6379 -n 1 llen celery


## Links I'm following
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
https://www.fullstackpython.com/celery.html
https://www.vinta.com.br/blog/2017/celery-overview-archtecture-and-how-it-works/
https://medium.com/analytics-vidhya/python-celery-explained-for-beginners-to-professionals-part-3-workers-pool-and-concurrency-ef0522e89ac5  --> good at explaining concepts
https://www.youtube.com/watch?v=Bo6UtRhedjE


## Notes
* Celery got a master process. Workers are Childs (worker processes).
* Concepts:
  - task is a function that does something (cooking)
  - worker (Cooker) is a program that execute tasks
  - A Task Queue is queue of tasks to be executed by workers (the order)
* if the child process dies, celery automatically creates a new one. If master process dies, you can restart it with supervisord
* Ofair: By default, preforking Celery workers distribute tasks to their worker processes (child) as soon as they are received, regardless of whether the process is currently busy with other tasks.
  This is a problem with tasks that might take too long. The -Ofair option disables this behavior, waiting to distribute tasks until each worker process is actually available for work.
  More info: https://medium.com/@taylorhughes/three-quick-tips-from-two-years-with-celery-c05ff9d7f9eb
* worker_prefetch_multiplier: The prefetch limit is a limit for the number of tasks (messages) a worker can reserve for itself (messages are available in memory).
  For long-running tasks this is a problem, so it's better to set it worker_prefetch_multiplier=1 (meaning it’ll only reserve one task per worker process at a time)
  Otherwise a bigger number can help in performance. If you have a combination of long- and short-running tasks, the best option is to use two worker nodes that are configured separately.
  More reading: https://docs.celeryq.dev/en/stable/userguide/optimizing.html
* Retry: Ideally task functions should be idempotent: meaning the function won’t cause unintended effects even if called multiple times with the same arguments.
  Since the worker cannot detect if your tasks are idempotent, the default behavior is to acknowledge the message in advance, just before it’s executed, so that a task invocation that already started is never executed again.
  You can explicitly add a retry loggic, but also you could use `acks_late` (worker acknowledge the message after the task returns instead)
  This brings other problems like a task running failing multiple times. More details: https://docs.celeryq.dev/en/master/userguide/tasks.html#tasks

## Idea: Build a program with following features
  - There's a celerybeat that runs every X minutes.
  - It hits an endpoint that get records info (it could get just the ID)
  - If you get just the ID, you add it to a new queue
  - One task reads the ID from the message and hits a new endpoint to get the entire record and save it.
  - If the message contains the entire record (instead of just the record ID), then it just saves it.
  - Is it better to do it in 2 steps? (first get the ID, then the rest, then save)
  - What would happen if the API return a bunch of records, should we implement batch?
  - Let's suppose the record needs some processing before saving. Should we do it in different steps (tasks)? task 1 process 1 --> task 2 process 2 --> etc
