#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  array.py Author "epy3" Date 22.07.2022

from opencl import OPENCL
from pow import POW


def main():
    # 1024 threads
    a = OPENCL(1024 * 1024)

    # diff & data
    diff = 67108863
    data = "118CC2121C3E641059BC1C2CFC45666C718CC2121C3E641059BC1C2CFC45666C"

    # set diff & data
    a.set_target(POW.difficulty_to_target(diff))
    a.set_data(data)

    while a.get_result() == 0:
        a.work()

    # check if result is valid
    print(POW.check_pow_nonce(diff, a.get_result_bytes(), a.str_data_to_bytes(data)))


if __name__ == "__main__":
    main()
