from celery import Celery

celery_app = Celery('app_name', broker='redis://redis_service')

def produce_messages_without_invoking_tasks():

    for i in range(50):
        celery_app.send_task('consumer.get_api_1', args=[i, i+1], kwargs={}, queue='pipeline_2')


if __name__ == '__main__':
    produce_messages_without_invoking_tasks()
