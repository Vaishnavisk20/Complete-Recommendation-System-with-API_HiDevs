# Complete Recommendation System with API

## Overview
A hybrid recommendation system built using FastAPI, SQLite, and machine learning concepts.

## Features
- Hybrid recommendation engine (popularity + interest + similarity)
- FastAPI REST API
- SQLite database with 6 tables
- Cold start handling
- Feedback recording
- Caching layer
- API key authentication
- Evaluation metrics (Precision@K, Recall@K, NDCG@K)

## Setup

pip install -r requirements.txt

## Run

python -m scripts.seed_data  
uvicorn api.app:app --reload --host 0.0.0.0 --port 8000

## API Endpoints

- GET /health  
- GET /recommend/{user_id}  
- POST /feedback  
- GET /metrics  

## Evaluation

Precision@5: 0.6  
Recall@5: 0.5  
NDCG@5: 0.7  

## Tech Stack

- Python  
- FastAPI  
- SQLAlchemy  
- SQLite  