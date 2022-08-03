#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  pow_class.py Author "epy3" Date 03.08.2022
from pydantic import BaseModel

class POW_data(BaseModel):
    """
    Stores the request data.
    """

    jsonrpc: str
    id: int
    method: str
    params: list

