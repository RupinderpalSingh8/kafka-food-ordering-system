import json
from kafka import KafkaConsumer, KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
# ORDER_LIMIT = 15

ORDER_CONFIMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092"

)
producer = KafkaProducer(
    bootstrap_servers = "localhost:9092"
)

print("Start listening")

while True:
    for message in consumer:
        print("Ongoing Transactions.....")
        consumer_message = json.loads(message.value.decode("utf-8"))
        print(consumer_message)
        #####  Above is reading of Transactions ###################
        
        ####### Order Confirmer ##########
        user_id =  consumer_message["user_id"]
        total_cost = consumer_message["total_cost"]
        
        data = {
            "customer_id" : user_id,
            "customer_email": f"{user_id}@gmail.com",
            "total_cost": total_cost
        }
        
        print("Successful Transactions")
        producer.send(
            ORDER_CONFIMED_KAFKA_TOPIC,
            json.dumps(data).encode('utf-8')
        )