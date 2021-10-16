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

    from configs import GrpcClientConfigs
    from grpc_server_client import create_rpc_client

    rpc = create_rpc_client(GrpcClientConfigs)
    users = rpc.get_users()
    print(users)

    return {"Hello": "Worldd"}


@app.get("/users}")
def read_item():
    from configs import GrpcClientConfigs
    from grpc_server_client import create_rpc_client

    rpc = create_rpc_client(GrpcClientConfigs)
    users = rpc.get_users()
    return users
