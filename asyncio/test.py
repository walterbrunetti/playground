

# https://www.integralist.co.uk/posts/python-asyncio/


"""
Concurrent Functions

The following functions help to co-ordinate the running of functions concurrently, and offer varying degrees of control dependant on the needs of your application.

"""


########## basic example #############
import asyncio

async def foo1():
    print("Foo!")

async def hello_world():
    await foo1()  # waits for `foo()` to complete
    print("Hello World!")

#asyncio.run(hello_world())
# Output:
# Foo!
# Hello World!



########## gather #############
"""wait for multiple asynchronous tasks to complete"""
async def foo2(n):
    await asyncio.sleep(5)  # wait 5s before continuing
    print(f"n: {n}!")


async def main2():
    tasks = [foo2(1), foo2(2), foo2(3)]
    await asyncio.gather(*tasks)


#asyncio.run(main2())

# Output
# n: 1!
# n: 2!
# n: 3!

########## wait #############
"""whichever task finishes first is what will be returned"""
from random import randrange


async def foo3(n):
    s = randrange(5)
    print(f"{n} will sleep for: {s} seconds")
    await asyncio.sleep(s)
    print(f"n: {n}!")


async def main3():
    tasks = [foo3(1), foo3(2), foo3(3)]
    result = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(result)


#asyncio.run(main3())

"""
2 will sleep for: 1 seconds
1 will sleep for: 0 seconds
3 will sleep for: 3 seconds
n: 1!
({<Task finished coro=<foo() done, defined at test.py:47> result=None>}, {<Task pending coro=<foo() running at test.py:50> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7f6048ff4a68>()]>>, <Task pending coro=<foo() running at test.py:50> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7f6048ff4ac8>()]>>})
"""


########## wait_for #############
"""utilize a timeout to prevent waiting endlessly for an asynchronous task to finish"""
async def foo4(n):
    await asyncio.sleep(10)
    print(f"n: {n}!")


async def main4():
    try:
        await asyncio.wait_for(foo4(1), timeout=5)
    except asyncio.TimeoutError:
        print("timeout!")


asyncio.run(main4())


########## as_completed #############
""" will yield the first task to complete, followed by the next quickest, and the next until all tasks are completed """

async def foo(n):
    s = randrange(10)
    print(f"{n} will sleep for: {s} seconds")
    await asyncio.sleep(s)
    return f"{n}!"


async def main():
    counter = 0
    tasks = [foo("a"), foo("b"), foo("c")]

    for future in asyncio.as_completed(tasks):
        n = "quickest" if counter == 0 else "next quickest"
        counter += 1
        result = await future
        print(f"the {n} result was: {result}")


asyncio.run(main())



