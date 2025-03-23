from fastapi import FastAPI
from typing import Dict

app = FastAPI(title="Achievement Tracker API")

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Achievement Tracker API is running"}

@app.get("/api/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)