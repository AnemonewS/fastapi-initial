from celery import Celery
from src.auth.utils import send_message

celery = Celery(
    'tasks',
    broker='redis://localhost:6379'
)


@celery.task
def send_message_to_email():
    send_message()
