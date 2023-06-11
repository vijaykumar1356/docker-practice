from confluent_kafka.admin import AdminClient, NewTopic
import socket

admin = AdminClient(
    conf={
        'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()
    }
)
futures = admin.create_topics([
    NewTopic(topic="users", num_partitions=2, replication_factor=1)
]) # returns {'topicname': future}


