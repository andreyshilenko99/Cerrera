# import socket
#
# from celery.exceptions import MaxRetriesExceededError
#
# from info.trace_info_getter2 import trace_info
# from celery import shared_task
# from Cerrera.celery import app
#
#
# @app.task(bind=True, default_retry_delay=1, name='trace', max_retries=500)
# def trace(self):
#     try:
#         res = trace_info()
#         if res == 0:
#             self.retry(countdown=5)
#     except (ConnectionRefusedError, BrokenPipeError, OSError, socket.timeout,  MaxRetriesExceededError) as e:
#         self.retry(exc=e, countdown=5)
#         print(e)
#
#
# trace.apply_async(queue='high_priority')
# trace.delay()