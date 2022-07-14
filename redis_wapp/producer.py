from consumer import add, do_something


def produce_messages():
    for i in range(50):
        add.delay(i, i+1) #.apply_async(queue="sf_streaming")
        do_something.delay()
