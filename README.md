# 🌎 Real-Time Environmental Data Lakehouse for Research and Analytics

> An end-to-end Data Engineering pipeline for ingesting, validating, processing, storing, and visualizing climate and environmental data — in real time and batch modes.

## 🚀 Overview

This project builds a real-time and batch-enabled pipeline to handle environmental sensor data collected across 22+ locations. The pipeline supports ingestion via Kafka, transformation using Airflow, validation with Great Expectations, storage in MySQL, and exposure via FastAPI & React.js.

> ✅ Built to simulate real-world data engineering workflows  
> ✅ Emphasizes data quality, pipeline orchestration, and API delivery  
> ✅ Deployed using Docker and optionally AWS

## 🔧 Tech Stack

| Layer              | Tool/Service             |
|-------------------|--------------------------|
| **Streaming**      | Apache Kafka             |
| **Processing**     | Apache Airflow, Python   |
| **Validation**     | Great Expectations       |
| **Storage**        | MySQL, AWS S3 (optional) |
| **API**            | FastAPI                  |
| **Frontend**       | React.js                 |
| **Monitoring**     | Prometheus, Grafana      |
| **Containerization** | Docker, Docker Compose  |
| **CI/CD**          | GitHub Actions           |

## 🧱 Architecture

```
[Sensors / CSV Files] → Kafka Producer → Kafka Topic (Raw Data)
                                     ↓
                             Kafka Consumer (validation & transformation)
                                     ↓
                            Staging Database (MySQL/PostgreSQL)
                                     ↓
                      Airflow DAG → Processed Data Warehouse
                                     ↓
                     FastAPI REST API → React Dashboard
                                     ↓
                            Researchers / Analysts
```

## 📂 Project Structure

```
climate-data-pipeline/
├── airflow/                # Airflow DAGs
├── api/                    # FastAPI backend
├── consumer.py             # Kafka Consumer
├── producer.py             # Kafka Producer
├── data/                   # Sample CSV files
├── frontend/               # React.js app
├── expectations/           # Great Expectations suite
├── docker-compose.yml      # Services definition
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .github/workflows/      # CI/CD with GitHub Actions
```

## 🗂️ Data Sources

- Simulated environmental sensor data (temperature, humidity, SWE, radiation, etc.)
- Historical `.csv` files used to simulate real-time streaming
- 22 unique location IDs

## 🔁 Pipeline Components

### 1. Kafka Producer

- Simulates streaming by reading `.csv` files line by line
- Publishes messages to the Kafka topic `climate_data_raw`

### 2. Kafka Consumer

- Listens to `climate_data_raw`
- Validates and transforms each message
- Writes cleaned records into staging MySQL table

### 3. Airflow DAG

- Scheduled batch ETL pipeline
- Cleans & loads data from staging → processed schema
- Integrates Great Expectations validation

### 4. FastAPI

- RESTful API to access processed data
- Supports:
  - Query by location & time
  - Data export
  - Attribute listing

### 5. React Dashboard

- Displays interactive charts for researchers
- Filters by:
  - Location
  - Timestamp range
  - Attribute type
- Data export to CSV supported

## ✅ Data Validation

Validation rules follow QA/QC protocols:

| Attribute         | Validation Rule |
|------------------|------------------|
| Air Temperature  | -35°C to 50°C    |
| RH               | 3% to 103%       |
| SWE              | ≥ 0              |
| SW/LW Radiation  | -0.4 to 1500     |
| Wind Speed       | 0 to 40 m/s      |
| ...              | Temporal rules, range checks, etc. |

> Real-time validation in Kafka Consumer  
> Batch validation via Great Expectations in Airflow

## ⚙️ Local Setup Instructions

### Prerequisites

- Docker & Docker Compose
- Python 3.9+
- Node.js & npm (for frontend)

### 1. Clone and Configure

```bash
git clone https://github.com/your-username/climate-data-pipeline.git
cd climate-data-pipeline
```

### 2. Start Services

```bash
# Start Kafka, Zookeeper, MySQL, Airflow
docker-compose up -d
```

### 3. Run Producer and Consumer

```bash
# Produce data
python producer.py --input data/sample_location.csv --topic climate_data_raw

# Consume data
python consumer.py --topic climate_data_raw
```

### 4. Launch API & Dashboard

```bash
# API
cd api
uvicorn main:app --reload

# Frontend
cd ../frontend
npm install
npm start
```

## 📊 Example API Usage

| Endpoint         | Method | Description              |
|------------------|--------|--------------------------|
| `/api/data`      | GET    | Query processed records  |
| `/api/export`    | GET    | Export to CSV            |
| `/api/locations` | GET    | List available locations |
| `/api/fields`    | GET    | List supported attributes|

## 📈 Monitoring (Optional)

- Kafka → Prometheus Kafka Exporter
- Airflow → Built-in + Prometheus
- MySQL → Grafana dashboard
- API → FastAPI metrics middleware

## 📌 Roadmap

- [ ] Schema registry with Avro  
- [ ] Anomaly detection in real-time  
- [ ] Snowflake or BigQuery integration  
- [ ] Auto-scaling via Kubernetes  
- [ ] Data cataloging with OpenMetadata  

## 📜 License

MIT License. Feel free to fork, modify, and build upon it.

## 🙌 Acknowledgments

- Inspired by real-world research challenges at UVM  
- Kafka, FastAPI, and Airflow documentation  
- Great Expectations open-source contributors  

## 👤 Author

**Jaya Prakash Narayana Raavi**  
Data Engineer & Full Stack Developer  
🔗 [LinkedIn](https://linkedin.com/in/your-profile)  
📧 your.email@example.com  


