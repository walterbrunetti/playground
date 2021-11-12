from consumer import add


def produce_some_messages():
    for i in range(1000):
        add.delay(i, i+1)




