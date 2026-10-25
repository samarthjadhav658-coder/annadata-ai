
from fastapi import FastAPI

app = FastAPI(
    title="Annadata AI API",
    description="Smart farming assistant for Maharashtra",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Annadata AI!",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
