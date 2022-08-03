#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  helper.py Author "epy3" Date 03.08.2022

class Helper:

    @staticmethod
    def is_hex(str):
        """
        is_hex:            Checks if string is a valid hex.
        :return:           True if valid hex, else False.
        """
        if len(str) % 2:
            return False

        hex_digits = set("0123456789abcdef")
        for char in str.lower():
            if not (char in hex_digits):
                return False
        return True

    @staticmethod
    def is_int(str):
        """
        is_int:            Checks if string is a valid int.
        :return:           True if valid int, else False.
        """
        for number in str:
            if not number.isdigit():
                return False
        return True
