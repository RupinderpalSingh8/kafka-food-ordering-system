# import json
# import time
# from uuid import uuid4
# from confluent_kafka import Producer

# ORDER_KAFKA_TOPIC = 'order_details'
# ORDER_LIMIT = 15

# producer_config = {'ootstrap.serbvers': 'localhost:9092'}
# producer = Producer(producer_config)

# print("Going to generate order after 10 seconds")
# print("Please wait for 10 seconds")

# def delivery_report(err, msg):
#     if err is not None:
#         print(f'Message delivery failed: {err}')
#     else:
#         print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# for i in range(1, ORDER_LIMIT):
#     data = {
#         "order_id": i,
#         "user_id": f"tom{i}",
#         "total_cost": i*2,
#         "items": "Burger, sandwich, pizza"
#     }
    
#     producer.produce(
#         ORDER_KAFKA_TOPIC,
#         key=str(i),
#         value=json.dumps(data),
#         callback=delivery_report
#     )
#     print(f"Sending.....{i}")
#     producer.flush()
#     time.sleep(10)
import json
import time

from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 1000

producer = KafkaProducer(bootstrap_servers="localhost:9092")

print("Going to be generating order after 3 seconds")
print("Will generate one unique order every 3 seconds")
time.sleep(10)

for i in range(1, ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i * 5,
        "items": "burger,sandwich,pizza",
    }

    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    # time.sleep(1) # will generate one unique order after every 10 seconds