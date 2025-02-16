# 🍔 Scalable Food Ordering System with Apache Kafka  

This project is a **scalable and event-driven backend system** for a food ordering application, built using **Apache Kafka** as the central message bus. It follows a **microservices architecture**, where each component is **loosely coupled** and communicates asynchronously via Kafka topics.

---

## 🔥 Key Features  

✅ **Event-Driven Architecture** – Uses Kafka for asynchronous message passing between services.  
✅ **Scalable & Decoupled Services** – Independent services can be scaled separately based on demand.  
✅ **Fault-Tolerant & Persistent Messaging** – Ensures reliability by persisting messages in Kafka.  
✅ **Extensible Design** – Easily add new services by subscribing to relevant Kafka topics.  

---

## 🛠 System Overview  

### 1️⃣ Orders Backend  
📌 **Function**: Handles order placement and publishes order details.  
- Simulates receiving an order from a client (e.g., mobile app).  
- Formats the order data and publishes it to the **`order_details`** Kafka topic.  

### 2️⃣ Transactions Backend  
📌 **Function**: Processes transactions and enriches order data.  
- Consumes messages from the **`order_details`** topic.  
- Simulates transaction processing and adds customer email.  
- Publishes a confirmation message to the **`order_confirmed`** Kafka topic.  

### 3️⃣ Email Backend  
📌 **Function**: Sends order confirmation emails.  
- Subscribes to the **`order_confirmed`** topic.  
- Simulates sending an email notification to the customer.  

---

## 🚀 Tech Stack  

- **Apache Kafka** – Message Broker  
- **Python / Node.js / Java** (Choose based on your implementation)  
- **Docker** (For containerization)  

---

## 🏗️ How to Run the Project  

1️⃣ **Start Kafka** (Ensure Zookeeper & Kafka Broker are running).  
2️⃣ **Run Each Service** independently, making sure they subscribe to the correct Kafka topics.  
3️⃣ **Simulate Order Placement** and track how messages propagate through the system.  
