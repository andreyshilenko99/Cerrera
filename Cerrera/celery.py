"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import
import os
from datetime import timedelta
import pika
from not_kringe_trace import decode_data_msg
from celery.app.control import Inspect
from kombu import Queue, Exchange
from info.skyPoint import skypoint
from Cerrera import settings
from Cerrera.settings import CELERY_BROKER_URL
from celery import Celery, shared_task

from info.trace_info_getter2 import trace_info

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cerrera.settings')
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

app = Celery('tasks')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

CELERYD_CONCURRENCY = 1
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_TACKS_LATE = False

# TODO ???
app.control.purge()

app.conf.task_queues = (
    Queue("for_aero", Exchange("for_aero"), routing_key="task_c"),
    # Queue("decode", Exchange("decode"), routing_key="task_z")
)
app.conf.task_routes = {
    'aeroScope': {'queue': 'for_aero', 'routing_key': 'task_c'},
    # 'decoder': {'queue': 'decode', 'routing_key': 'task_z'}
}
app.conf.beat_schedule = {
    # 'decoder': {
    #     'task': 'decoder',
    #     'schedule': timedelta(seconds=3),
    # },
    'aeroScope': {
        'task': 'aeroScope',
        'schedule': timedelta(seconds=2),
    },
}


# @app.task(default_retry_delay=1, name='decoder', max_retries=500)
# def decode():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#
#     def callback(ch, method, properties, body):
#         data = decode_data_msg(body)
#         print(data)
#
#     channel.queue_declare(queue='messages')
#     # channel.basic_publish(exchange='',
#     #                       routing_key='messages',
#     #                       body=b'Hello World!')
#     # print(" [x] Sent 'Hello World!'")
#     # connection.close()
#     channel.basic_consume(queue='messages',
#                           auto_ack=True,
#                           on_message_callback=callback)
#     channel.start_consuming()
#     # connection.close()


# decode.apply_async(queue='high_priority')


@shared_task(name='aeroScope')
def aeroScope():
    skypoint()
