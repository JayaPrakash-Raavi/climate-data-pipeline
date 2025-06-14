from kafka import KafkaConsumer
import mysql.connector
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Load MySQL configs
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    port=int(os.getenv("MYSQL_PORT"))
)

cursor = db.cursor()

# Kafka Consumer
consumer = KafkaConsumer(
    os.getenv("KAFKA_TOPIC"),
    bootstrap_servers=os.getenv("KAFKA_BROKER"),
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Waiting for messages...")

for msg in consumer:
    record = msg.value
    print("Received:", record)

    sql = """
    INSERT INTO table1 (TIMESTAMP, Location, AirTC_Avg, RH)
    VALUES (%s, %s, %s, %s)
    """
    values = (
        record["TIMESTAMP"],
        record["Location"],
        float(record["AirTC_Avg"]),
        float(record["RH"])
    )

    try:
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        print("DB Insert Error:", e)
