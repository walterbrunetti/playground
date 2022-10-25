import random
import celery
from celery.utils.log import get_task_logger

from celery_app import celery_app
from core.hit_service import hit_service, hit_other_service, hit_extra_service
from core.rss_service import get_cnn_rss as get_cnn_rss_service


logger = get_task_logger(__name__)


class BaseTask(celery.Task):
    """
        Here you can:
        Record time and memory performance
        Sentry exceptions
        Additional logging
    """
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('ERROR: {0!r} failed: {1!r}'.format(task_id, exc))


@celery_app.task(base=BaseTask)
def get_api_1(x, y):
    return hit_service(x, y)


@celery_app.task(bind=True, max_retries=2, default_retry_delay=5, base=BaseTask)
def get_api_2(self):
    """
    Task will raise a ValueError if max retries is reached.
    """
    try:
        hit_other_service()
        # test failure scenarios
        if random.uniform(1, 5) <= 3:
            raise ValueError("damn it")
    except ValueError as exc:
        logger.warning("Something wrong happened")
        raise self.retry(exc=exc)


@celery_app.task(bind=True, max_retries=2, default_retry_delay=5, base=BaseTask)
def get_api_3(self):
    hit_extra_service()


@celery_app.task(base=BaseTask)
def get_cnn_rss():
    return get_cnn_rss_service()
