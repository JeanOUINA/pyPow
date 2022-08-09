#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  nonce_test.py Author "epy3" Date 09.08.2022
import asyncio
import pytest
from nonce import NONCE

DBADDR = "public/nodes.db"


def test_database_read():
    db = NONCE.read_database(DBADDR)
    assert len(db) > 0


def test_database_read_err():
    with pytest.raises(Exception):
        NONCE.read_database(DBADDR + "123")
        assert True


def test_race():
    db = NONCE.read_database(DBADDR)
    diff = "60612441"
    target = "35c82fe515c2982c5ef75226eab35f3fb14952f8ef59005f02893Cd3dca4db00"

    result = asyncio.run(NONCE.race(diff, target, db, 5))
    assert result["result"] != "error"


def test_race_err():
    db = NONCE.read_database(DBADDR)
    diff = "60612441"
    target = "35c82fe515c2982c5ef75226eab35f3fb14952f8ef59005f02893Cd3dca4db00"

    result = asyncio.run(NONCE.race(diff, target, db, 0.1))
    assert result["result"] == "error"


if __name__ == "__main__":
    pass
