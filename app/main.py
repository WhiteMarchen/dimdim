from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")

def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/change/custNum/industryType.do?year=2020&month=11&metroCd=11&apiKey=0CB11KB41AcMhjdEFnMr022xxsApomXZd3qD9m92&returnType=json"    
    contents = requests.get(URL).text

    return { "message": contents}

@app.get("/home")
def home():
    return { "message": "Home!" }