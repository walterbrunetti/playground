
from celery import Celery

def init_app():
    celery_app = Celery('app_name', broker='redis://redis_service', include=["consumer",])
    celery_app.conf.task_default_queue = "default"  # rename default queue from `celery` to something else
    #celery_app.conf.task_routes = {'consumer.*': {'queue': 'pipeline_2'}}
    celery_app.conf.task_routes = ([
        ('consumer.get_api_1', {'queue': 'pipeline_2'}),
        ('consumer.get_api_2', {'queue': 'pipeline_1'}),
        ('consumer.get_api_3', {'queue': 'pipeline_1'}),
        ('consumer.get_cnn_rss', {'queue': 'pipeline_3'}),
    ],)  # this is for the producer
    return celery_app

celery_app = init_app()
