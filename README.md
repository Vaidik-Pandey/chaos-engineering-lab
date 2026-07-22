# 🐒 Chaos Engineering Lab

Chaos Engineering system replicating practices used by 
Netflix, Amazon and Google — automated fault injection,
self-healing infrastructure and real-time monitoring.

## Architecture

Flask App (3 replicas)
↓
Chaos Monkey → Kills random container every 30s
↓
Auto Healer → Detects failure, restarts in <10s
↓
Prometheus → Collects metrics
↓
Grafana → Live dashboard
↓
Incident Reporter → JSON reports


## Tech Stack
- **Python Flask** — Sample microservices
- **Docker** — Containerization
- **Chaos Monkey** — Automated fault injection
- **Prometheus** — Metrics collection
- **Grafana** — Real-time visualization
- **Auto Healer** — Self-healing infrastructure

## Features
- ✅ Automated fault injection every 30 seconds
- ✅ Self-healing recovery in under 10 seconds
- ✅ Real-time Grafana monitoring dashboard
- ✅ Automated JSON incident report generation
- ✅ Replicates Netflix Chaos Monkey practices

## Project Structure

chaos-engineering-lab/
├── app/ # Flask microservices
├── chaos/ # Chaos Monkey implementation
├── monitoring/ # Prometheus + Grafana config
├── reports/ # Auto-generated incident reports
└── docker-compose.yml


## Screenshots
View screenshots folder

## How to Run
```bash
# Start all services
docker-compose up -d

# Run Chaos Monkey
python chaos/chaos_monkey.py

# View dashboard
http://localhost:3000
```

## How it Works
1. Flask app runs as 3 Docker containers
2. Chaos Monkey randomly kills one every 30s
3. Auto Healer detects failure and restarts it
4. Prometheus tracks recovery time
5. Grafana shows live metrics
6. Incident Reporter logs every event to JSON
