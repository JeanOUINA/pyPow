#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  info.py Author "epy3" Date 22.07.2022

import pyopencl as cl

class GPU:

    @staticmethod
    def get_info():
        for p in cl.get_platforms():
            print('=' * 50)
            print('Platform - Name:     ' + p.name)
            print('Platform - Vendor:   ' + p.vendor)
            print('Platform - Profile:  ' + p.profile)
            for d in p.get_devices():
                print('Device - Name:       ', d.name)
            print('=' * 50)


if __name__ == "__main__":
    GPU.get_info()
