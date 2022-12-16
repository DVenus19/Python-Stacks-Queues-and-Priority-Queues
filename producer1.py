import pika

QUEUE_NAME = "mailbox"

with pika.BlockingConnection() as connection:

