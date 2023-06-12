from confluent_kafka import Consumer
import socket

consumer = Consumer({
        'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname(),
        'group.id': 'test',
        "default.topic.config": {"auto.offset.reset": "smallest"},
        "enable.auto.commit": True,
    })

topic = 'users'
consumer.subscribe(['users'])
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        # Initial message consumption may take up to
        # `session.timeout.ms` for the consumer group to
        # rebalance and start consuming
        print("Waiting...")
    elif msg.error():
        print("ERROR: %s".format(msg.error()))
    else:
        # Extract the (optional) key and value, and print.
        print(f"Consumed event from topic {msg.topic()}: key={msg.key().decode('utf-8')} value={msg.value().decode('utf-8')} partition={msg.partition()}")
