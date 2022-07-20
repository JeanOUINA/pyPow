#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  pow.py Author "epy3" Date 20.07.2022

from Crypto.Random import get_random_bytes
from hashlib import blake2b


class POW:
    @staticmethod
    def check_pow_nonce(diff: int, nonce: bytes, data: bytes) -> bool:
        """
        check_pow_nonce:        Calculates if hash (nonce+data) < target.
        :param diff:            Difficulty in int.
        :param nonce:           Nonce in 'little' endian byte array.
        :param data:            Data in byte array.
        :return:                Returns true if nonce is good.
        """
        target = POW.difficulty_to_target(diff)
        out = POW.pow_hash256(nonce, data)
        return POW.quick_greater(out, int.to_bytes(target, 32, "big"))

    @staticmethod
    def get_pow_nonce(diff: int, data: bytes) -> bytes:
        """
        get_pow_nonce:          Calculates a nonce from diff + data.
                                (!) Warning: this is an infinite loop.
        """
        target = POW.difficulty_to_target(diff)
        target = int.to_bytes(target, 32, "big")

        while len(target) == 32:
            nonce = get_random_bytes(8)
            out = POW.pow_hash256(nonce, data)
            if POW.quick_greater(out, target):
                return nonce
        return bytes(0)

    @staticmethod
    def pow_nonce_random_range(diff: int, data: bytes, tries: int) -> bytes:
        """
        pow_nonce_random_range: Calculates a nonce from diff + data from
                                a random range.
        :param tries:           Number of tries.
        """
        target = POW.difficulty_to_target(diff)
        target = int.to_bytes(target, 32, "big")

        for _ in range(0, tries):
            nonce = get_random_bytes(8)
            out = POW.pow_hash256(nonce, data)
            if POW.quick_greater(out, target):
                return nonce
        return bytes(0)

    @staticmethod
    def pow_nonce_random_range_fast(target: bytes, data: bytes, tries: int) -> bytes:
        """
        pow_nonce_random_range: Calculates a nonce from diff + data from
                                a random range.
        :param tries:           Number of tries.
        """
        for _ in range(0, tries):
            nonce = get_random_bytes(8)
            out = POW.pow_hash256(nonce, data)
            if POW.quick_greater(out, target):
                return nonce
        return bytes(0)

    @staticmethod
    def pow_nonce_num_range(diff: int, data: bytes, begin: int, end: int) -> bytes:
        """
        pow_nonce_num_range:    Calculates a nonce from diff + data from
                                a range of given numbers.
        :param begin:           Start of range.
        :param end:             End of range.
        """
        target = POW.difficulty_to_target(diff)
        target = int.to_bytes(target, 32, "big")

        for i in range(begin, end):
            nonce = int.to_bytes(i, 8, "big")
            out = POW.pow_hash256(nonce, data)
            if POW.quick_greater(out, target):
                return nonce
        return bytes(0)

    @staticmethod
    def pow_hash256_from_hash(hash: blake2b, nonce: bytes, data: bytes) -> bytes:
        """
        pow_hash256_from_hash:  Blake2b object update and digest with nonce + data.
        """
        hash.update(nonce + data)
        return hash.digest()

    @staticmethod
    def pow_hash256(nonce: bytes, data: bytes) -> bytes:
        """
        pow_hash256:            Blake2b hash in 32 bit from nonce + data.
        """
        hash = blake2b(digest_size=32)
        hash.update(nonce + data)
        return hash.digest()

    @staticmethod
    def difficulty_to_target(diff: int) -> int:
        """
        difficulty_to_target:   Calculates given  difficulty to target:
                                target = 2^256 / (1 + (1 / difficulty))
        """
        out = 1 / diff
        out += 1
        return int(pow(2, 256) / out)

    @staticmethod
    def target_to_difficulty(tar: int) -> int:
        """
        target_to_difficulty:   Calculates given target to difficulty
        """
        out = pow(2, 256) / tar
        out -= 1
        return int(1 / out)

    @staticmethod
    def quick_inc(arr: bytearray) -> bytes:
        """
        quick_inc:              Increases bytearray by one (+1).
        """
        # fuck python
        temp = int.from_bytes(arr, "big") + 1
        try:
            temp = temp.to_bytes(len(arr), "big")
        except:
            temp = temp.to_bytes(len(arr) + 1, "big")[1:]
        finally:
            return temp

    @staticmethod
    def quick_greater(byte_x: bytes, byte_y: bytes, size: int = 32) -> bool:
        """
        quick_greater:          Checks if (array) x is greater than y.
        """
        for i in range(0, size):
            if byte_x[i] > byte_y[i]:
                return True
            if byte_x[i] < byte_y[i]:
                return False
        return False

    @staticmethod
    def pad_to_32bytes(data: bytes, left: bool = True) -> bytes:
        """
        pad_to_32bytes:         Pad bytes array to 32bit bytes array.
        :param left:            True to pad on the left, false pad on the right.
        """
        ret = bytearray(data)
        while len(ret) < 32:
            ret.insert(0, 0) if left else ret.append(0)
        return ret


if __name__ == "__main__":
    exit()
