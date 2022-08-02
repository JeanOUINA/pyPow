#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  test.py Author "epy3" Date 21.07.2022
from pow.pow import POW
from gpu.opencl import OPENCL

import timeit

LOOPS = 1

def main():
    params = [
        67108863,
        "118CC2121C3E641059BC1C2CFC45666C718CC2121C3E641059BC1C2CFC45666C",
    ]
    diff = params[0]
    data = bytearray.fromhex(params[1])

    # test with cpu
    start = timeit.default_timer()

    for _ in range(0, LOOPS):
        result = POW.get_pow_nonce(diff, data)
        print(f"CPU: RESULT: {POW.check_pow_nonce(diff, result, data)}")

    stop = timeit.default_timer()
    print("CPU:", stop - start)
    cpu = stop - start

    # test with gpu
    a = OPENCL("gpu/blake.cl")
    a.set_target(POW.difficulty_to_target(diff))
    a.set_data(params[1])

    # stat gpu test
    start = timeit.default_timer()
    for _ in range(0, LOOPS):
        while a.get_result() == 0:
            a.work()
        print(f"CPU: RESULT: {POW.check_pow_nonce(diff, a.get_result_bytes(), data)}")
        a.reset()

    stop = timeit.default_timer()
    print("GPU:", (stop - start))
    gpu = stop - start

    if gpu < cpu:
        print(f"GPU: {cpu // gpu}x faster")

if __name__ == "__main__":
    main()
