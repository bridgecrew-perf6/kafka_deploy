#!/usr/bin/python3.5
# let's send data to kafka topic
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(10):
    data = {'number' : e}
    producer.send('test-topic', value=data)
    sleep(1)
