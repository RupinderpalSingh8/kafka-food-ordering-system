import json

from kafka import KafkaConsumer

ORDER_CONFIMED_KAFKA_TOPIC = "order_confirmed"


consumer = KafkaConsumer(
    ORDER_CONFIMED_KAFKA_TOPIC,

    bootstrap_servers="localhost:9092"

)

email_sent = set()
print("Email is listening")

while True:
    for message in consumer:
        consumer_details = json.loads(message.value.decode())
        customer_email = consumer_details["customer_email"]

        print(f"Sending email to {customer_email}")
        
        email_sent.add(customer_email)
        print(f"Email sent to {len(email_sent)}, unique emails.")