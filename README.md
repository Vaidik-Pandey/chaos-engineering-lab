# 🐒 Chaos Engineering Lab

## Overview
A real-world DevOps project implementing Chaos Engineering
principles used by Netflix, Amazon and Google.

## Tech Stack
- Python Flask, Docker, Prometheus, Grafana
- Chaos Monkey, Auto Healer, Incident Reporter

## Features
- Live monitoring dashboard
- Automated fault injection
- Self-healing infrastructure
- Automatic incident reporting

## Architecture
Flask App → Prometheus → Grafana Dashboard
Chaos Monkey → Kills containers every 30s
Auto Healer → Detects & restarts in <10s
Incident Reporter → Generates JSON reports
