# AI Lead Qualification + Smart Response System

## Overview
This project is a FastAPI-based AI Lead Qualification System designed to classify incoming leads and generate personalized responses.

The system accepts lead input through an API endpoint, classifies the lead as HOT, WARM, or COLD, and generates a business-focused response.

----------------------------

## Features

- Lead classification
- Personalized response generation
- FastAPI REST API
- Swagger API documentation
- Production-aware architecture
- Input validation using Pydantic
- Simple scalable design

------------------------------

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---------------------------------

## API Endpoint

### POST /classify-lead

Example Request:

```json
{
  "name": "Kavya",
  "company": "ABC Groups",
  "budget": 90000,
  "requirement": "Need AI chatbot urgently",
  "urgency": "high"
}
```

----------------------------------

## Lead Classification Logic

- HOT → High budget + high urgency
- WARM → Medium budget
- COLD → Low budget / low urgency

-----------------------------------

## Production Considerations

- Retry handling
- Fallback responses
- Monitoring & logging
- Scalable API design
- CRM/DB integration support
- Async queue support

-----------------------------------

## Future Improvements

- LLM integration
- Vector database
- Redis queue
- Real CRM integration
- Multi-model lead scoring