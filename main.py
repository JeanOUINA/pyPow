#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  main.py Author "epy3" Date 18.07.2022

from fastapi import FastAPI
from pydantic import BaseModel
from gpu.opencl import OPENCL
from pow.pow import POW
import base64

app = FastAPI()

#OPENCL settings
ocl = OPENCL("gpu/blake.cl")


class POW_request(BaseModel):
    jsonrpc: str
    id: int
    method: str
    params: list


@app.post("/api/work/")
def run_pow(req: POW_request):
    ocl.reset()
    ocl.set_workgroup_size(256)
    ocl.set_threads(4096 * ocl.get_workgroup_size())

    ocl.set_target(POW.difficulty_to_target(int(req.params[0])))
    ocl.set_data(req.params[1])
    while ocl.get_result() == 0:
        ocl.work()

    result = base64.b64encode(ocl.get_result_bytes())
    return {"jsonrpc": req.jsonrpc, "id": req.id, "result": result}
