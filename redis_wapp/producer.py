from consumer import get_api_1, get_api_2, get_api_3, get_cnn_rss


def produce_messages():
    for i in range(50):
        get_api_1.delay(i, i+1) #.apply_async(queue="sf_streaming")
        get_api_2.delay()
        get_api_3.delay()

    for i in range(50):
        get_cnn_rss.delay()
