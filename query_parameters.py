from fastapi import FastAPI

from typing import Optional

from enum import Enum

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# Optional QP 
@app.get("/players/{player_id}")
async def read_player(player_id: int, q: Optional[str] = None) -> dict:
    response = {"player_id": str(player_id)}
    if q:
        response["q"] = q
    return response

# Type Conversion: 1, True, true, on, yes
@app.get("/monsters/{monster_id}")
async def read_monster(monster_id: str, q: Optional[str] = None, short: bool = False):
    monster = {"monster_id": monster_id}
    if q:
        monster.update({"q": q})
    if not short:
        monster.update(
            {"description": "This is an amazing monster that has a long description"}
        )
    return monster


# Required Parameters 
class ProductVariantSize(str, Enum):
    S = 's'
    M = 'm'
    L = 'l'


class ProductVariantColor(str, Enum):
    black = 'black'
    white = 'white'
    green = 'green'


# Required Parameters just by NOT defining a default value (such as None or other)
@app.get("/products/{product_id}/variants/{variant_id}")
async def read_product_variant(product_id: int, variant_id: int, color: ProductVariantColor, size: ProductVariantSize):
    product_variant = {"product_id": product_id, "variant_id": variant_id, "color": color.value, "size": size.value}
    return product_variant