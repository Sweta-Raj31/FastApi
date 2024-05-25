from celery import Celery

celery_app = Celery(
    "pdf_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.task_routes = {"app.tasks.*": {"queue": "pdf_queue"}}
