from enum import Enum
from pydantic import BaseModel
from typing import Union

from fastapi import FastAPI


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class ModelName(str, Enum):
    efficientnet = "efficientnet"
    resnet = "resnet"
    yolo = "yolo"



@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.efficientnet:
        return {"model_name": model_name, "message": f'Load Model: {model_name}'}

    if model_name.value == "resnet":  # model_name.value.resnet
        return {"model_name": model_name, "message": f'Load Model: {model_name}'}

    return {"model_name": model_name, "message": f'Load Model: {model_name}'}


@app.get("/datasets/{data_path:path}")
async def get_data(data_path: str):
    return {"data_path": data_path}


@app.get("/datasets/{data}/info/{mode}")
async def get_data_info(data: str, mode: str):
    info = {"data": data, "info": mode}
    return info



