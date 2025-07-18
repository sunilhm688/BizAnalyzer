from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agents import analyze_website

app = FastAPI()

# Allow requests from any frontend (adjust later if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WebsiteInput(BaseModel):
    url: str

@app.post("/analyze")
async def analyze(input_data: WebsiteInput):
    try:
        result = analyze_website(input_data.url)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
