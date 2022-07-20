#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  addr.py Author "epy3" Date 19.07.2022
from hashlib import blake2b


class ADDR:
    @staticmethod
    def get_body(address: str) -> str:
        """
        get_body:                   Returns the body of address.
                                    These are the 5->45 bytes.
        """
        # todo: validity check
        return address[5:45]

    @staticmethod
    def get_checksum(address: str) -> str:
        """
        get_checksum:               Returns the checksum of address.
        """
        # todo: validity check
        return address[45:]

    @staticmethod
    def get_checksum_from_body(body: str) -> str:
        """
        get_checksum_from_body:     Calculates the checksum from body.
                                    Returns the hexadecimal value.
        """
        # todo: validity check
        ret = bytearray.fromhex(body)
        hash = blake2b(digest_size=5)
        hash.update(ret)

        return hash.hexdigest()
