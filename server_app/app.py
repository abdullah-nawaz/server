import os
import requests
from typing import Optional

from fastapi import FastAPI

from server_app.common.utils import init_sec_client

app = FastAPI()


@app.get("/")
def read_root():
    client = init_sec_client()
    res = client.read_root_get()
    print(res)

    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}