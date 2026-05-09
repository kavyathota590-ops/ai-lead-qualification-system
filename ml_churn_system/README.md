# ML Churn Prediction System

## Overview

This project is a production-oriented ML prediction system built using FastAPI.

The system predicts customer churn risk based on customer activity and engagement data.

---------------------------

## Features

- Customer churn prediction
- FastAPI REST API
- Input validation
- Production-aware design
- Scalable architecture
- Structured prediction responses

----------------------------------------

## Tech Stack

- Python
- FastAPI
- Pydantic
- Scikit-learn
- Pandas

---------------------------------------

## API Endpoint

### POST /predict-churn

Example Request:

```json
{
  "age": 30,
  "monthly_spend": 1200,
  "support_tickets": 4,
  "usage_hours": 6
}
```

------------------------------------------

## Prediction Logic

- Low usage
- High support complaints
- Low spending

These indicators increase churn probability.

-------------------------------------------------

## Sample Output

The system returns both:
- Churn classification
- Risk score for interpretability

Example:

{
  "prediction": "MEDIUM CHURN RISK",
  "risk_score": 6
}

------------------------------------------

## Future Improvements

- Real ML model training
- Feature engineering
- Model monitoring
- Drift detection
- Kubernetes deployment
- CI/CD pipelines