from confluent_kafka import Producer
import socket
import random

producer = Producer({
        'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()
    })
user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']


def delivery_callback(err, msg):
    if err:
        print('ERROR: Message failed delivery: {}'.format(err))
    else:
        print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))


for i in range(10):
    key = random.choice(user_ids)
    producer.produce(
        topic='users',
        value=random.choice(products),
        key=key,
        partition=1 if key[0].lower() > 'n' else 0,
        on_delivery=delivery_callback
    )

producer.flush()
