#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  helper.py Author "epy3" Date 03.08.2022

class Helper:
    @staticmethod
    def valid_input(diff: str, data: str):
        """
        valid_input:        Checks if input is valid.
        :return:            Returns true if valid else False.
        """
        if (
            not Helper.is_int(diff)
            or not 1 <= int(diff) <= 1000108864
            or not Helper.is_hex(data)
            or len(data) != 64
        ):
            return False
        return True

    @staticmethod
    def is_hex(input: str):
        """
        is_hex:            Checks if string is a valid hex.
        :return:           True if valid hex, else False.
        """
        if len(input) % 2:
            return False

        hex_digits = set("0123456789abcdef")
        for char in input.lower():
            if not (char in hex_digits):
                return False
        return True

    @staticmethod
    def is_int(input: str):
        """
        is_int:            Checks if string is a valid int.
        :return:           True if valid int, else False.
        """
        for number in input:
            if not number.isdigit():
                return False
        return True

if __name__ == "__main__":
    exit()
