from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float

    def calculate_total_price(self):
        total_price = self.price + self.price * self.tax 
        return total_price


app = FastAPI()

# Define the endpoint and pass the body data as Pydantic Model 

# Advantages: e
"""
Read the body as JSON
Convert the types, if needed 
Validate the data >> Return error if it is invalid
As you are using Pydantic 
"""

@app.post("/items/")
async def create_item(item: Item) -> dict:
    # Code Support
    # item.name + item.price
    return {
        "name": item.name.upper(),
        "tax_value": item.price * item.tax,
        "total_price": item.calculate_total_price()
        }


from enum import Enum


class Monster(BaseModel):
    """BaseModel to create a Monster"""
    name: str
    type: Optional[str] = None
    description: str
    weapon: str
    strenght: int = 100


class MonsterType(str, Enum):
    WIZZARD = 'wizzard'
    ORC = 'orc'
    CENTAUR = 'centaur'


# Request body + path + query parameters 
# If the parameter is declared in path, it will be used as path parameter
# if parameter is of singular type
@app.post("/monster/{type}")
async def create_monster(type: MonsterType, monster: Monster, q: Optional[str] = None):
    monster.type = type
    result = {**monster.dict()}
    if q:
        result.update({"q": q})
    return result




