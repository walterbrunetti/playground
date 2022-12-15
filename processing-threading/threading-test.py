
#!/usr/bin/env python
"""
Threading - concurrency

The order in which threads are run is determined by the operating system and can be quite hard to predict. It may (and likely will) vary from run to run, so you need to be aware of that when you design algorithms that use threading.

Be careful with race conditions between threads. You can use locks for dealing with this problem.

https://realpython.com/intro-to-python-threading/  --> concepts and examples
https://superfastpython.com/threading-in-python/  --> well at explaining concepts


The Python process will terminate once all (non background threads) are terminated.
- Process: An instance of the Python interpreter has at least one thread called the MainThread.
- Thread: A thread of execution within a Python process, such as the MainThread or a new thread.


"""


import logging
import threading
import time
import concurrent.futures


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(4)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


    # first approach
    #threads = list()
    #for index in range(3):
    #    logging.info("Main    : create and start thread %d.", index)
    #    x = threading.Thread(target=thread_function, args=(index,))
    #    threads.append(x)
    #    x.start()

    #for index, thread in enumerate(threads):
    #    logging.info("Main    : before joining thread %d.", index)
    #    thread.join()
    #    logging.info("Main    : thread %d done", index)


    # better approach
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))

