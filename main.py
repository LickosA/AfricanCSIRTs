from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()
BD = './BD/Africa.json'

class Csirt(BaseModel):
    pass

@app.get("/")
def read_root():
    return {"Hello": "Welcome to African CSIRT API"}


@app.get("/cities")
async def list_cities():
    with open(BD) as f:
        data = json.load(f)
    cities = list(data.keys())
    return {"cities": cities}

@app.get("/csirts")
async def list_csirt():
    with open(BD) as f:
        data = json.load(f)
    csirts = [value['team'] for value in data.values()]
    return {'csirts':csirts}

@app.get("/city_csirt/{city}")
async def csirt_by_city(city:str):
    with open(BD) as f:
        data = json.load(f)
    if city not in data.keys():
        return {'error':'Invalid city name'}
    return {city:data[city]}

@app.get('/csirt/{name}')
async def csirt_by_name(name:str):
    with open(BD) as f:
        data = json.load(f)
    for value in data.values():
        if value['team']==name:
            return {name:value}
    return {'error':'Invalid csirt name'}

@app.get('/all_data')
async def all_data():
    with open(BD) as f:
        data = json.load(f)
    return {'data':data}

@app.post('/csirt')
async def create_csirt(csirt:Csirt):
    return csirt
