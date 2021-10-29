from typing import List, Optional

from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class AvatarType(str, Enum):
    JEDI = 'JEDI'
    STORMTROOPER = 'STORMTROOPER'
    SITH = 'SITH'
    MANDALORIAN = 'MANDALORIAN'
    EWOK = 'EWOK'

class AvatarSize(str, Enum):
    SMALL = 'small'
    MEDIDUM = 'medium'
    LARGE = 'large'


class Avatar(BaseModel):
    name: str
    weapons: List[str] = []
    type: AvatarType


@app.post("/package-with-quantity/")
def pack_avatar_with_quantity(
    avatar: Avatar, 
    quantity: int = Query(..., gt=0, lt=10),  # Elipsis
    delivery: bool = Query(False, description="The package has delivery"), 
    size: AvatarSize = AvatarSize.SMALL):
    return {"message": f"Packing {avatar.name} in size {size}", 
            "delivery": delivery,
            "quantity": quantity
        }




@app.post("/package/")
def pack_avatar(avatar: Avatar, delivery: bool = False, size: str = "small"):
    return {"message": f"Packing {avatar.name} in size {size}", 
            "delivery": delivery
        }


@app.post("/package-with-selector/")
def pack_avatar_with_selector(avatar: Avatar, delivery: bool = Query(
    False, description="The package has delivery"), size: AvatarSize = AvatarSize.SMALL):
    return {"message": f"Packing with selector {avatar.name} in size {size}", 
            "delivery": delivery
        }


@app.post("/avatar/")
def create_avatar(avatar: Avatar):
    return {
        "message": f"creating {avatar.name}",
        "avatar_weapons": avatar.weapons
    }

@app.post("/avatars/")
def load_avatars(avatars: List[Avatar]):
    all_weapons = []
    for avatar in avatars:
        for weapon in avatar.weapons:
            all_weapons.append(weapon)


@app.get("/")
def read_root():
    return {"message": "Hello clicOH World from FastAPI"}


@app.get("/avatars/{avatar_id}")
def read_avatar(avatar_id: int, q: str = None):
    return {"avatar_id": avatar_id, "q": q}




