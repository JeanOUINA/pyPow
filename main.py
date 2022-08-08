#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  main.py Author "epy3" Date 18.07.2022

import asyncio
import nest_asyncio

from fastapi import FastAPI
from gpu.opencl import OPENCL
from pow.pow import POW
from servers.servers import SERV
from util.helper import Helper
from util.pow_class import POW_data

nest_asyncio.apply()
APP = FastAPI()
OCL = OPENCL("gpu/blake.cl")
DB = SERV.read_node_database("servers/servers.db")


@APP.post("/")
async def run_pow(req: POW_data):
    """
    Processing API Post.
    """
    # check for valid input
    if (
        not Helper.is_int(req.params[0])
        or int(req.params[0]) < 1
        or int(req.params[0]) > 67108863
        or not Helper.is_hex(req.params[1])
        or len(req.params[1]) != 64
    ):
        return {"jsonrpc": req.jsonrpc, "id": req.id, "result": "input error"}

    tasks = []
    result = "error"

    OCL.set_target(POW.difficulty_to_target(int(req.params[0])))
    OCL.set_data(req.params[1])

    #FIXME: not working
    #tasks.append(SERV.nonce_race(req.params[0], req.params[1], DB, 5))
    tasks.append(OCL.work())

    while tasks:
        done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for _done in done:
            result = _done.result()
            break
        break

    return {"jsonrpc": req.jsonrpc, "id": req.id, "result": result}


if __name__ == "__main__":
    pass
