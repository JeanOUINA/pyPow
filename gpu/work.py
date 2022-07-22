#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  array.py Author "epy3" Date 22.07.2022

import numpy as np
import pyopencl as cl
import pyopencl.array as pycl_array

context = cl.create_some_context()
queue = cl.CommandQueue(context)

mf = cl.mem_flags

a = 0x00000
a = a.to_bytes(32, 'big')
b = 0x0000f
b = b.to_bytes(32, 'big')

prg = cl.Program(context, open('blake2b.cl').read()).build()

a_gpu = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
b_gpu = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)

prg.blake256_hash_block(queue, [0,0], None, a_gpu, b_gpu)

print("a: {}".format(a))
print("b: {}".format(b))
