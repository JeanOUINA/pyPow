#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  main.py Author "epy3" Date 09.08.2022

from fastapi import FastAPI, Request
from gpu.opencl import OPENCL
from log.logger import LOGGER
from pow.pow import POW
from util.helper import Helper
from util.pow_data import POW_data

# global variables
APP = FastAPI()
OCL = OPENCL("gpu/blake.cl")
LOG = LOGGER.setup("log/logfile")


@APP.post("/")
def run_pow(req: POW_data, client: Request):
    """
    Processing API Post.
    """
    # set input variables
    diff = req.params[0]
    data = req.params[1]

    # log request
    LOG.info(f"ip={client.client.host} diff={diff} data={data}")

    # validate input
    if not Helper.valid_input(diff, data):
        return {"jsonrpc": req.jsonrpc, "id": req.id, "result": "input error"}

    # setup en run opencl
    OCL.set_target(POW.difficulty_to_target(int(diff)))
    OCL.set_data(data)
    result = OCL.work()

    # return result
    return {"jsonrpc": req.jsonrpc, "id": req.id, "result": result}


if __name__ == "__main__":
    exit()
