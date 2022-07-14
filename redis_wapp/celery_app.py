
from celery import Celery

def init_app():
    celery_app = Celery('app_name', broker='redis://redis_service', include=["consumer",])
    celery_app.conf.task_default_queue = "pipeline_2"
    #celery_app.conf.task_routes = {'consumer.*': {'queue': 'pipeline_2'}}
    celery_app.conf.task_routes = ([
        ('consumer.add', {'queue': 'pipeline_2'}),
        ('consumer.do_something', {'queue': 'pipeline_1'}),
    ],)
    return celery_app

celery_app = init_app()
