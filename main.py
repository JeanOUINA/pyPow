#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  main.py Author "epy3" Date 18.07.2022

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class POW_request(BaseModel):
    jsonrpc: str
    id: int
    method: str
    params: list


@app.post("/api/generatework/")
async def create_item(req: POW_request):
    return {"jsonrpc": req.jsonrpc, "id": req.id, "result": "test"}
