import pika
from not_kringe_trace import decode_data_msg


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def callback(ch, method, properties, body):
    data = decode_data_msg(body)
    print(data)


channel.queue_declare(queue='messages')
# channel.basic_publish(exchange='',
#                       routing_key='messages',
#                       body=b'Hello World!')
# print(" [x] Sent 'Hello World!'")
# connection.close()
channel.basic_consume(queue='messages',
                      auto_ack=True,
                      on_message_callback=callback)
channel.start_consuming()
connection.close()
