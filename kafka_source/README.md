```bashs
apt install mdp zip unzip -y

apt install openjdk-8-jdk -y



useradd -m kafka -d /home/kafka -s /bin/bash



touch /etc/default/kafka

cp zookeeper-server.service /etc/systemd/system/zookeeper-server.service

cp kafka@.service /etc/systemd/system/kafka@.service

chmod -x /etc/systemd/system/kafka@.service /etc/systemd/system/zookeeper-server.service

systemctl daemon-reload




cp -R kafka_1001 /etc

cp -R kafka_1002 /etc

cp -R kafka_1003 /etc

chown -R kafka:kafka /etc/kafka_100?




for i in {1001..1003}; do mkdir /var/lib/kafka$i; done

chown kafka:kafka /var/lib/kafka100?




cp kafka.zip ~/kafka.zip

md5sum kafka.zip 

b0e726dfbcca7e2a92be9e828738dea5

sha256sum kafka.zip

856d970fa24a02fbc285d616e31426d95002dc69c57608b6852f5b4e627f78e6

sha1 kafka.zip
a325d354407db712a912510ca81e39af1989e37c
7dc37f78572ced62591d253819b5e3dca971e23e


cd /usr/lib

unzip /root/kafka.zip

chown kafka:kafka kafka

cd ~



service zookeeper-server restart

for i in {1001..1003}; do service kafka@$i restart; done

systemctl enable zookeeper-server

for i in {1001..1003}; do systemctl enable kafka@$i restart; done



apt install ufw

ufw enable

ufw open ports 22, 2281, 9092-9097
```