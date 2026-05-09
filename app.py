from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Input schema
class Lead(BaseModel):
    name: str
    company: str
    budget: int
    requirement: str
    urgency: str

# Health check route
@app.get("/")
def home():
    return {"message": "AI Lead Qualification System Running"}

# Main API endpoint
@app.post("/classify-lead")
def classify_lead(lead: Lead):

    # Lead Classification Logic
    if lead.budget >= 5000 and lead.urgency.lower() == "high":
        lead_type = "HOT"

    elif lead.budget >= 2000:
        lead_type = "WARM"

    else:
        lead_type = "COLD"

    # Personalized Response Generation
    response = f"""
    Hi {lead.name},

    Thank you for contacting us regarding {lead.requirement}.

    Based on your business requirements, our team believes we can help your company achieve faster results.

    Our team will contact you shortly for the next steps.

    Regards,
    AI Sales Team
    """

    # Simulated DB log
    lead_data = {
        "name": lead.name,
        "company": lead.company,
        "lead_type": lead_type,
        "timestamp": str(datetime.now())
    }

    return {
        "status": "success",
        "lead_data": lead_data,
        "generated_response": response
    }