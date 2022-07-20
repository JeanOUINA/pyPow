#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  test.py Author "epy3" Date 21.07.2022
from pow.pow import POW
import multiprocessing as mp

async_result = 0

def get_nonce(diff: bytes, data: bytes):
    return POW.pow_nonce_random_range_fast(diff, data, 10000)

def get_nonce_cb(result):
    global async_result
    async_result += int.from_bytes(result, 'big')


def generate_result(diff: bytes, data: bytes):
    global async_result

    while not async_result:
        pool = mp.Pool(mp.cpu_count())
        for _ in range(mp.cpu_count()):
            pool.apply_async(get_nonce, args=(diff, data), callback=get_nonce_cb)
        pool.close()
        pool.join()

    return str(async_result)


if __name__ == "__main__":
    params = ["67108863", "35c82fe515c2982c5ef75226eab35f3fb14952f8ef59005f02893cd3dca4db09"]

    diff = int(params[0])
    data = bytearray.fromhex(params[1])

    target = POW.difficulty_to_target(diff)
    target = int.to_bytes(target, 32, "big")

    nonce = generate_result(target, data)

    print(nonce)
