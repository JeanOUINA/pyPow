#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  pow_data.py Author "epy3" Date 09.08.2022
from pydantic import BaseModel


class POW_data(BaseModel):
    """
    Stores the request data.
    """

    jsonrpc: str
    id: int
    method: str
    params: list
