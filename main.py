from fastapi import FastAPI, HTTPException

from enum import Enum, auto
from dataclasses import dataclass

app = FastAPI()

@app.get("/")
async def root():
    return {'message': "Hello world!!!!"}

inventory = {
    1: {
        'name': 'Rappi Card',
        'price': 4.00,
        'brand': 'White brand'
    }, 
    2: {
        'name': 'Bottle',
        'price': 3.00,
        'brand': 'Nalgene'
    }, 
}

@app.get("/get_item/{item_id}")
def get_inventory(item_id: int):
    _inventory = inventory.get(item_id)
    if not _inventory:
        raise HTTPException(status_code=404, detail='Item not found')        
    return _inventory

# Data Validation: Try passing a foo to the endpoint /items/
@app.get("/items/{item_id}")
async def get_item(item_id: int) -> dict:
    return {"item_id": item_id}

# Order matters, path are evaluated in order
@app.get("/users/foo")
async def read_user_foo() -> dict:
    return {'user_id': "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    return {'user_id': user_id}


# Predefined values >>> SHOWN in the documentation
class ModelName(str, Enum):
    """ENUM class that represents model names"""
    alexnet = "alexnet"
    resnet = "resnet" 
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> dict:
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Return Enumerations Values
model_name = ModelName('alexnet')

print(model_name)
print(model_name.value)
print(ModelName.lenet.value)





