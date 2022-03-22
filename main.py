from lib.Model import Model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


class Prediction(BaseModel):
    Text: str


app = FastAPI()
model = Model()



@app.post("/predict")
async def prediction(text):
    clean_text = model.clean_data(text)
    vect = model.vectorizer(clean_text)
    y_pred = model.predict(vect)
    if y_pred == 0:
        return 'this text was written by an teen'
    else:
        return 'this text was written by an adult'


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
