import random

from celery_app import celery_app
from core.hit_service import hit_service, hit_other_service
from core.rss_service import get_cnn_rss as get_cnn_rss_service

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


class BaseTask:
    """
    Record time and memory performance
    Sentry exceptions
    Additional logging
    """
    pass


@celery_app.task() # name="add", base=BaseTask
def add(x, y):
    return hit_service(x, y)


@celery_app.task(bind=True, max_retries=2, default_retry_delay=5)
def do_something(self):
    """
    Task will raise a ValueError if max retries is reached.
    Task needs to be idempotent to be retried.
    """
    try:
        hit_other_service()
        if random.uniform(1, 5) <= 2:
            raise ValueError("damn it")
    except ValueError as exc:
        logger.warning("Something wrong happened")
        raise self.retry(exc=exc)


@celery_app.task
def get_cnn_rss():
    return get_cnn_rss_service()
