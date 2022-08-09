#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  nonce.py Author "epy3" Date 09.08.2022

import requests
import json
import asyncio


class NONCE:
    @staticmethod
    async def race(diff: str, target: str, nodes: list, timeout: float) -> dict:
        """
        race:                       Finds and returns the fastest response
                                    from a list of PoW servers.
        :param diff:                Difficulty in string format.
        :param target:              Target in string format.
        :param nodes:               List of PoW Nodes servers.
        :param timeout:             Timeout in seconds.
        :return: [dict]             Nonce in base64 from fastest server.
        """
        tasks = []
        nonce = {}

        for node in nodes:
            tasks.append(
                asyncio.create_task(NONCE.get_response(diff, target, node, timeout))
            )

        while tasks:
            done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            for _done in done:
                nonce = json.loads(_done.result())
                for task in tasks:
                    task.cancel()
                break
            break
        # FIXME: proper shutdown of running threads.
        return nonce

    @staticmethod
    async def get_response(diff: str, target: str, URL: str, timeout: float) -> str:
        """
        get_response:               Sends a POST request and returns response.
        :param diff:                Difficulty in string format.
        :param target:              Target in string format.
        :param URL:                 URL of the PoW Node.
        :param timeout:             Timeout in seconds.
        :return:                    Json string.
        """
        headers = {
            "accept": "text/plain;charset=UTF-8",
            "content-type": "application/json",
        }
        data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "util_getPoWNonce",
            "params": [
                diff,
                target,
            ],
        }
        try:
            return requests.post(URL, headers=headers, json=data, timeout=timeout).text
        except:
            return json.dumps({"jsonrpc": "2.0", "id": "1", "result": "error"})

    @staticmethod
    def read_database(db: str) -> list:
        """
        read_database:              Converts a text database to a list.
        :param db:                  Name of the database file.
        :return: [list]             List of nodes in sting format.
        """
        database = open(db, "r")
        public_nodes = database.read().split("\n")[:-1]
        database.close()
        return public_nodes


if __name__ == "__main__":
    exit()
