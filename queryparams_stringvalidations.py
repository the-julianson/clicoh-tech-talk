from typing import Optional, List

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=5)):
    results = {"items": "items"}
    if q:
        results.update({"q": q})
    return results

# Other validators: min_length gt ge lt le regex

@app.get("/asados/")
async def organize_asado(q: Optional[str] = Query(None, regex="^hagamo un asado tomemo fernet$"), description="Una descripcion"):
    result = 'Que hacemo esta noche?'
    if q:
        result = result + " " + q
    else: 
        result = result + ".... :("
    return result

@app.get("/monsters/")
async def read_monsters(
    q: List[str] = Query(
        None,
        title="List of words",
        description="The query will concatenate this and form a sentence"
        )
    ):
    query_items = {"q": q}
    the_string = ''
    try:
        for elem in q:
            the_string += (" " + elem)
    except TypeError:
        the_string = 'Bueno, a codear nomas!'

    return the_string
