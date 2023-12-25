import json
import re
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model_predection import predict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

class Data_aspect(BaseModel):
    text: str
    length: int = 20

@app.post("/predict")
async def summary(data: Data_aspect):
    """Predict the summary of a story"""
    try:
        clean_text = re.sub(r'\s+', ' ', data.text)
        clean_text = re.sub(r'[^\x00-\x7F]+', '', clean_text)
        summary_text = predict(clean_text, data.length).encode('unicode_escape').decode('utf-8')
        
        result = {"Summary": summary_text}
        json_result = JSONResponse(content=json.dumps(result, ensure_ascii=False))
        return json_result
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
async def root():
    return {"message": "Hello! You are connected to the API of the project"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""
    return {"result": num1 + num2}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
