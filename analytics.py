import json

from kafka import KafkaConsumer

ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092"
)

total_order_count = 0
total_revenue = 0

print("Analytics listening....")

while True:
    for message in consumer:
        print("Updating Analytics......") 
        consumer_details = json.loads(message.value.decode())
        
        total_cost = float(consumer_details["total_cost"])
        total_order_count += 1
        total_revenue += total_cost
        
        print(f"Orders so far today {total_order_count}")
        print(f"Revenue generated so far today {total_revenue}")