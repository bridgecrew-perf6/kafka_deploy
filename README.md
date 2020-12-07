# Recovery

## Fixing

1. Intsall openjdk 1.8
```bash
apt install openjdk-8-jdk -y
```
<br />

2. Fix systemd kafka
```bash
touch /etc/default/kafka
```
<br />

3. Open closed ports of zookeeper and kafka
```bash
iptables -t filter -D INPUT 1
iptables -t filter -D INPUT 1
iptables -t filter -D INPUT 1
iptables-save
```
<br />

## Checking
1. Restart services
```bash
service zookeeper-server restart
for i in {1001..1003}; do service kafka@$i restart; done
```
<br />

2. Make sure that's working
```bash
service zookeeper-server status
for i in {1001..1003}; do service kafka@$i status; done
```
<br />

3. Create test topic
```bash
 /usr/lib/kafka/bin/kafka-topics.sh --create \
--zookeeper localhost:2181 \
--topic test-topic \
--replication-factor 1 \
--partitions 1
```
<br />

4. Make sure that's working
```bash
/usr/lib/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181
```
<br />

## Processing
1. Install kafka python libs
```bash
apt install python3-pip -y
pip3 install kafka --user
```
<br />

2. Make consumer and producer scripts
```bash
cat << EOF > kafka_produce_generate.py
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
EOF
```
<br />

```bash
cat << EOF > kafka_consume_generate.py
#!/usr/bin/python3.5
# let's get data from kafka topic
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'test-topic',
     bootstrap_servers=['localhost:9092'],
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print (message)
EOF
```
<br />

3. Run it
```bash
chmod +x kafka_produce_generate.py kafka_consume_generate.py
./kafka_produce_generate.py & ./kafka_consume_generate.py
```
<br />

## Finish
<img src="https://github.com/pid998877/kafka_deploy/blob/main/pic/pexels-pixabay-210881.jpg?raw=true" width="800px" height="auto">
<br />