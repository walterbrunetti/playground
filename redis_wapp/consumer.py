from celery_app import celery_app
from core.hit_service import hit_service, hit_other_service
from core.rss_service import get_cnn_rss as get_cnn_rss_service


@celery_app.task
def add(x, y):
    return hit_service(x, y)


@celery_app.task
def do_something():
    return hit_other_service()


@celery_app.task
def get_cnn_rss():
    return get_cnn_rss_service()
