# ")!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  opencl.py Author "epy3" Date 02.08.2022
import numpy as np
import pyopencl as cl
import pyopencl.array as arr

from pow import POW
from random import getrandbits


class OPENCL:
    def __init__(self, threads: int = 1024) -> None:
        self.threads = threads

        self._data = np.zeros(32, dtype=np.uint8)
        self._nonce = np.zeros(1, dtype=np.uint64)
        self._target = np.zeros(32, dtype=np.uint8)
        self._result = np.zeros(1, dtype=np.uint64)

        self.context = cl.create_some_context()
        self.queue = cl.CommandQueue(self.context)
        self.prog = cl.Program(self.context, open("blake.cl").read()).build()

        self._data_buf: arr.Array
        self._nonce_buf: arr.Array
        self._target_buf: arr.Array
        self._result_buf = arr.to_device(self.queue, self._result)

    def work(self):
        self.set_nonce()

        _temp = self.prog.vitechain_work(
            self.queue,
            (self.threads,),
            (1,),
            self._nonce_buf.data,
            self._data_buf.data,
            self._target_buf.data,
            self._result_buf.data,
        )
        _temp.wait()

        self._result = self._result_buf.get()

    def set_data(self, data: str) -> None:
        _temp = bytearray.fromhex(data)
        self._data = np.array(list(_temp), dtype=np.uint8)
        self._data_buf = arr.to_device(self.queue, self._data)

    def set_nonce(self) -> None:
        self._nonce = np.array(getrandbits(64), dtype=np.uint64)
        self._nonce_buf = arr.to_device(self.queue, self._nonce)

    def set_target(self, target: int) -> None:
        _temp = int.to_bytes(target, 32, "big")
        self._target = np.array(list(_temp), dtype=np.uint8)
        self._target_buf = arr.to_device(self.queue, self._target)

    def get_data(self) -> np.ndarray:
        return self._target

    def get_nonce(self) -> np.ndarray:
        return self._nonce

    def get_target(self) -> np.ndarray:
        return self._target

    def get_result(self) -> np.ndarray:
        return self._result

    def get_result_bytes(self) -> bytes:
        return int.to_bytes(int(self._result), 8, "little")

    def print_result(self) -> None:
        print(int(self._result[0]))

    @staticmethod
    def str_data_to_bytes(data: str) -> bytes:
        return bytearray.fromhex(data)


if __name__ == "__main__":
    exit()
