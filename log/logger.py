#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  logger.py Author "epy3" Date 09.08.2022

import logging


class LOGGER:
    @staticmethod
    def setup(logfile: str) -> logging.Logger:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s | %(message)s")

        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger


if __name__ == "__main__":
    exit()
