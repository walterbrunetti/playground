from consumer import add, do_something, get_cnn_rss


def produce_messages():
    for i in range(50):
        add.delay(i, i+1) #.apply_async(queue="sf_streaming")
        do_something.delay()

    for i in range(50):
        get_cnn_rss.delay()
