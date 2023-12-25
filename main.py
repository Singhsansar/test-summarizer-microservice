import uvicorn 
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from model_predection import predict

app = FastAPI()

class Data_aspect(BaseModel):
    text: str
    length: int = 500


@app.post("/predict")
async def summary(data: Data_aspect):
    print(f"predict_story accepted json payload: {data}")
    summary = predict(data.text, data.length)
    print(f"The result is the following payload: {summary}")
    payload = {"Summary": summary.tolist()[0]}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "Hello You are connected to the API of the project"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')