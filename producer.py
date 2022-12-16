from kafka3 import KafkaProducer
producer = KafkaProducer(bootstrap_servers="local:9092")
while True :
    message = input("Message: ")
    producer.send(topic="datascience", value=message.encode("utf-8"))