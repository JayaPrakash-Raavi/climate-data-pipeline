from kafka import KafkaProducer
import pandas as pd
import time
import json

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Load the CSV file
df = pd.read_csv('data/sample_location.csv')

# Send each row to Kafka topic
for _, row in df.iterrows():
    message = row.to_dict()
    producer.send('climate_data_raw', value=message)
    print(f"Sent: {message}")
    time.sleep(1)  # wait 1 second to simulate real-time
