from kafka import KafkaConsumer
import mysql.connector
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connect to MySQL database
try:
    db = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=int(os.getenv("MYSQL_PORT"))
    )
    cursor = db.cursor()
    print("✅ Connected to MySQL")
except mysql.connector.Error as err:
    print(f"❌ Error connecting to MySQL: {err}")
    exit(1)

# Connect to Kafka
try:
    consumer = KafkaConsumer(
        os.getenv("KAFKA_TOPIC"),
        bootstrap_servers=os.getenv("KAFKA_BROKER"),
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    print("✅ Kafka Consumer is listening...")
except Exception as e:
    print(f"❌ Kafka error: {e}")
    exit(1)

# Process messages from Kafka
for msg in consumer:
    record = msg.value
    print("📥 Received:", record)

    sql = """
    INSERT INTO table1 (TIMESTAMP, Location, AirTC_Avg, RH)
    VALUES (%s, %s, %s, %s)
    """
    values = (
        record.get("TIMESTAMP"),
        record.get("Location"),
        float(record.get("AirTC_Avg", 0)),
        float(record.get("RH", 0))
    )

    try:
        cursor.execute(sql, values)
        db.commit()
        print("✅ Inserted into MySQL")
    except Exception as e:
        print("❌ DB Insert Error:", e)
