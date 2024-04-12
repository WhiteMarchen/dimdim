from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    born : int
    age : int

item_data = Item(name = " ", born = 0, age = 0)

@app.post("/items/")
def create_item(name : str, born : int):
    global item_data
    item_data.name = name
    item_data.born = born
    return item_data

@app.get("/item/")
def read_item():
    global item_data
    return item_data

@app.put("/item/")
def update_item(age : int):
    global item_data
    item_data.age = age
    return item_data

@app.delete("/item/")
def delete_item():
    global item_data
    del item_data.born, item_data.age
    return item_data