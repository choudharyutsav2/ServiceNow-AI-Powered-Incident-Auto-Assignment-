# AI-Powered Incident Auto-Assignment

## Overview
This project builds an AI-powered system to automatically detect semantically similar incidents in ServiceNow and assign new incidents to the most appropriate support group. It uses a Sentence Transformer model to understand the meaning of incidents, even when the wording differs, helping reduce resolution time and manual effort.

## Problem
Manual incident routing often leads to:
- Wrong assignment groups
- Duplicate troubleshooting
- Delayed resolution
- SLA breaches

## Solution
The system compares new incidents with historical resolved incidents using semantic similarity. If a close match is found, the incident is auto-assigned to the group that previously resolved the issue, along with contextual reference details.

## How It Works
1. Incident is created in ServiceNow
2. Business Rule triggers on creation
3. Incident data is sent to AI service via ngrok
4. AI model finds the most similar resolved incident
5. Assignment group is returned
6. Incident is auto-assigned with reference work notes

## Tech Stack
- ServiceNow (ITSM, Business Rules)
- Python & Flask (AI Service)
- Sentence Transformers (all-MiniLM-L6-v2)
- Cosine Similarity
- Pandas
- ngrok
- CSV (historical incident data)

## Setup (Quick)
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m src.app
ngrok http 5000


