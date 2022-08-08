import numpy as np
import pyopencl as cl
import pyopencl.array as arr

from random import getrandbits
import base64


class OPENCL:
    def __init__(self, path: str = "blake.cl") -> None:

        self._data = np.zeros(32, dtype=np.uint8)
        self._nonce = np.zeros(1, dtype=np.uint64)
        self._target = np.zeros(32, dtype=np.uint8)
        self._result = np.zeros(1, dtype=np.uint64)

        self.context = cl.create_some_context()
        self.queue = cl.CommandQueue(self.context)
        self.prog = cl.Program(self.context, open(path).read()).build()
        self.kernel = self.prog.all_kernels()[0]

        self._data_buf: arr.Array
        self._nonce_buf: arr.Array
        self._target_buf: arr.Array
        self._result_buf = arr.to_device(self.queue, self._result)

        self._work_group = self.kernel.get_work_group_info(
            cl.kernel_work_group_info.WORK_GROUP_SIZE, self.prog.devices[0]
        )
        self._threads = 4096 * self._work_group

    async def work(self) -> bytes:
        """
        work:               Finds and returns a valid nonce.
        :return:            Returns the nonce as base64.
        """
        self.reset()
        while self.get_result() == 0:
            self.set_nonce()

            _temp = self.prog.work(
                self.queue,
                (self._threads,),
                (self._work_group,),
                self._nonce_buf.data,
                self._data_buf.data,
                self._target_buf.data,
                self._result_buf.data,
            )
            _temp.wait()
            self._result = self._result_buf.get()

        return base64.b64encode(self.get_result_bytes())

    def reset(self) -> None:
        """
        reset:              Resets the current result buffer and
                            sets a new random nonce buffer.
        """
        self.set_nonce()
        self._result = np.zeros(1, dtype=np.uint64)
        self._nonce_buf = arr.to_device(self.queue, self._nonce)
        self._result_buf = arr.to_device(self.queue, self._result)

    def set_data(self, data: str) -> None:
        """
        set_data:           Sets the input data from string and
                            updates the buffer on the GPU.
        :param data:        Data string in hex notation.
        """
        _temp = bytearray.fromhex(data)
        self._data = np.array(list(_temp), dtype=np.uint8)
        self._data_buf = arr.to_device(self.queue, self._data)

    def set_nonce(self) -> None:
        """
        set_nonce:          Sets a new random 64bit nonce and
                            updates the buffer on the GPU.
        """
        self._nonce = np.array(getrandbits(64), dtype=np.uint64)
        self._nonce_buf = arr.to_device(self.queue, self._nonce)

    def set_target(self, target: int) -> None:
        """
        set_target:         Sets a new target and updates the buffer on the GPU.
        :param target:      Target or threshold in integer.
        """
        _temp = int.to_bytes(target, 32, "big")
        self._target = np.array(list(_temp), dtype=np.uint8)
        self._target_buf = arr.to_device(self.queue, self._target)

    def set_threads(self, threads: int) -> None:
        """
        set_threads:        Sets a number of global workers.
        :param threads:     Number of workers in integer.
        """
        self._threads = threads

    def set_work_size(self, size: int) -> None:
        """
        set_work_size:      Sets the workgroup_size (local).
        :param size:        Size of workgroup in integer.
        """
        self._work_group = size

    def get_data(self) -> np.ndarray:
        """
        get_data:           Returns the current data information.
        :return:            32 byte numpy array[32].
        """
        return self._target

    def get_nonce(self) -> np.ndarray:
        """
        get_nonce:          Returns the current nonce.
        :return:            64 bit numpy array[1].
        """
        return self._nonce

    def get_target(self) -> np.ndarray:
        """
        get_target:         Returns the current target.
        :return:            32 byte numpy array[32].
        """
        return self._target

    def get_result(self) -> np.ndarray:
        """
        get_result:         Returns the current result.
        :return:            64 bit numpy array[1].
        """
        return self._result

    def get_threads(self) -> int:
        """
        get_threads:        Returns the current number of threads.
        :return:            Number of threads as integer.
        """
        return self._threads

    def get_work_size(self) -> int:
        """
        get_work_size:      Returns the size of the workgroup.
        :return:            Size of workgroup as integer.
        """
        return self._work_group

    def get_result_bytes(self) -> bytes:
        """
        get_result_bytes:   Returns the current result.
        :return:            Result as bytes array.
        """
        return int.to_bytes(int(self._result), 8, "little")


if __name__ == "__main__":
    exit()
