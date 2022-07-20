#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  addr_test.py Author "epy3" Date 19.07.2022
from addr import ADDR
from hashlib import blake2b
import pytest


def test_string_hash():
    addr = "vite_ab24ef68b84e642c0ddca06beec81c9acb1977bbd7da27a87a"
    prev = "0000000000000000000000000000000000000000000000000000000000000000"
    out = "8689fc3e7d0bcad0a1213fd90ab53437ce745408750f7303a16c75bad28da8c3"

    addr_arr = bytearray.fromhex(ADDR.get_body(addr) + "00")
    prev_arr = bytearray.fromhex(prev)
    out_arr = bytearray.fromhex(out)

    hash = blake2b(digest_size=32)
    hash.update(addr_arr + prev_arr)
    assert hash.digest() == out_arr


def test_all():
    addr = "vite_ab24ef68b84e642c0ddca06beec81c9acb1977bbd7da27a87a"
    body = ADDR.get_body(addr)
    sum = ADDR.get_checksum(addr)

    assert ADDR.get_checksum_from_body(body) == sum


if __name__ == "__main__":
    pass
