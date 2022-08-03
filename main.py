#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  main.py Author "epy3" Date 18.07.2022

from fastapi import FastAPI
from gpu.opencl import OPENCL
from pow.pow import POW
from util.helper import Helper
from util.pow_class import POW_data

APP = FastAPI()
OCL = OPENCL("gpu/blake.cl")


@APP.post("/")
def run_pow(req: POW_data):
    """
    Processing API Post.
    """
    # check for valid input
    if (
        not Helper.is_int(req.params[0])
        or int(req.params[0]) < 1
        or int(req.params[0]) > 67108863
        or not Helper.is_hex(req.params[1])
    ):
        return {"jsonrpc": req.jsonrpc, "id": req.id, "result": "input error"}

    # set target, set data
    OCL.set_target(POW.difficulty_to_target(int(req.params[0])))
    OCL.set_data(req.params[1])

    # find nonce
    result = OCL.work()

    return {"jsonrpc": req.jsonrpc, "id": req.id, "result": result}


if __name__ == "__main__":
    pass
