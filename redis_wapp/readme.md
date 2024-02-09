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
- App and Containers are working correctly.
- Flower is showing workers but not queues for some reason.
- there's an endpoint that produces 50 messages.
- there are 4 tasks and 3 queues. Two of the tasks share a queue (`pipeline_1`)
- there are 2 consumers (workers). One consume from queue 1 and 2. The other from queue 3.
- created a separate container (`producer_service`) to produce messages without access to the code base.

Next steps:
- Add a bunch of messages at once and see how it behaves when adding more workers.
  * Use fixed number of workers (vs autoscaling)  -- does it refer to concurrency?
  * use ofair
- rate_limit
- Dependencies between tasks: Chains - groups - chords  (when is convenient to use each?)
- monitoring celery/tasks (flower - new rellic/data dog/ graphite-grafana/logentries)
  * https://flower.readthedocs.io/en/latest/prometheus-integration.html#start-grafana
- supervisord
- Mitigate problems with Celery. See fixes here: https://steve.dignam.xyz/2023/05/20/many-problems-with-celery/


# Redis commands
redis-cli -h redis_service -p 6379 -n 1 llen celery


## Links I'm following
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
https://www.fullstackpython.com/celery.html
https://www.vinta.com.br/blog/2017/celery-overview-archtecture-and-how-it-works/
https://medium.com/analytics-vidhya/python-celery-explained-for-beginners-to-professionals-part-3-workers-pool-and-concurrency-ef0522e89ac5  --> good at explaining concepts
https://www.youtube.com/watch?v=Bo6UtRhedjE


## Notes & learnings
* Celery got a master process. Workers are Childs (worker processes).
* Concepts:
  - task is a function that does something (cooking)
  - worker (Cooker) is a program that execute tasks
  - A Task Queue is queue of tasks to be executed by workers (the order)
* if the child process dies, celery automatically creates a new one. If master process dies, you can restart it with supervisord
* Ofair: 
  ```By default, preforking Celery workers distribute tasks to their worker processes (child) as soon as they are received, regardless of whether the process is currently busy with other tasks.
  This is a problem with tasks that might take too long. The -Ofair option disables this behavior, waiting to distribute tasks until each worker process is actually available for work.
  More info: https://medium.com/@taylorhughes/three-quick-tips-from-two-years-with-celery-c05ff9d7f9eb
  ```
* worker_prefetch_multiplier: 
  ```The prefetch limit is a limit for the number of tasks (messages) a worker can reserve for itself (messages are available in memory).
  For long-running tasks this is a problem, so it's better to set it worker_prefetch_multiplier=1 (meaning it’ll only reserve one task per worker process at a time)
  Otherwise a bigger number can help in performance. If you have a combination of long- and short-running tasks, the best option is to use two worker nodes that are configured separately.
  More reading: https://docs.celeryq.dev/en/stable/userguide/optimizing.html
  ```
* Retry: 
  ```Ideally task functions should be idempotent: meaning the function won’t cause unintended effects even if called multiple times with the same arguments.
  Since the worker cannot detect if your tasks are idempotent, the default behavior is to acknowledge the message in advance, just before it’s executed, so that a task invocation that already started is never executed again.
  You can explicitly add a retry loggic, but also you could use `acks_late` (worker acknowledge the message after the task returns instead)
  This brings other problems like a task running failing multiple times. More details: https://docs.celeryq.dev/en/master/userguide/tasks.html#tasks
  ```
* Stopping a worker: 
  ```Shutdown should be accomplished using the TERM signal (kill -15) so it gracefully kill the process.
  This means it will wait the worker to finish executing jobs before killing it.
  If the worker won’t shutdown after considerate time, for being stuck in an infinite-loop or similar, you can use the KILL signal (-9) to force terminate the worker: but be aware that currently executing tasks will be lost (i.e., unless the tasks have the acks_late option set).
  https://docs.celeryq.dev/en/master/userguide/workers.html#worker-stopping
  ```
* Calling tasks: 
  ```
  delay is our beloved shortcut to apply_async taking star-arguments. apply_async provides multiple options.
  A signature() wraps the arguments, keyword arguments, and execution options of a single task invocation in a way such that it can be passed to functions or even serialized and sent across the wire.
  https://docs.celeryq.dev/en/stable/userguide/canvas.html#guide-canvas
  ```

## Idea: Build a program with following features
  - There's a celerybeat that runs every X minutes.
  - It hits an endpoint that get records info (it could get just the ID)
  - If you get just the ID, you add it to a new queue
  - One task reads the ID from the message and hits a new endpoint to get the entire record and save it.
  - If the message contains the entire record (instead of just the record ID), then it just saves it.
  - Is it better to do it in 2 steps? (first get the ID, then the rest, then save)
  - What would happen if the API return a bunch of records, should we implement batch?
  - Let's suppose the record needs some processing before saving. Should we do it in different steps (tasks)? task 1 process 1 --> task 2 process 2 --> etc
