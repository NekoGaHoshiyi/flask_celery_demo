from kombu import Exchange, Queue
from celery.schedules import crontab
from datetime import timedelta


BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/3"
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_RESULT_EXPIRES = 24*3600
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TIMEZONE = "Asia/Shanghai"

CELERYD_MAX_TASKS_PER_CHILD = 400
CELERYD_MAX_MEMORY_PER_CHILD = 300000


CELERY_IMPORTS = (
    "app",
)

CELERY_QUEUES = (
    Queue("q_copy_files", Exchange("q_copy_files"), routing_key="q_copy_files"),
)

CELERY_ROUTES = {
    "app.*": {"queue": "q_copy_files", "routing_key": "q_copy_files"},
}

