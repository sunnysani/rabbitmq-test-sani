#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('sender', 'sender123')
parameters = pika.ConnectionParameters('34.69.147.3',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='sani')

channel.basic_publish(exchange='', routing_key='sani', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()