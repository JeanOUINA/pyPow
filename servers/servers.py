#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  servers.py Author "epy3" Date 08.08.2022
# -*- coding: utf-8 -*-
#  servers.py Author "epy3" Date 08.08.2022
import requests
import json
import asyncio


class SERV:
    @staticmethod
    async def nonce_race(diff: str, target: str, db: list, t: float = 2) -> str:
        """
        nonce_race:                 Gets the nonce from public PoW Nodes in database.
                                    Returns the first result.
                                    This function uses multiple CPU threads.
        :param diff:                Difficulty in string format.
        :param target:              Target in string format.
        :param db:                  Database name. Default = servers.db
        :param t:                   Timeout in seconds.
        :return:                    Returns the first base64 result.
        """
        result = asyncio.run(SERV.find_nonce(diff, target, db, t))

        return result["result"]

    @staticmethod
    def read_node_database(db: str) -> list:
        """
        read_node_database:         Converts a text database to a list.
        :param db:                  Name of the database file.
        :return: [list]             List of nodes in sting format.
        """
        database = open(db, "r")
        public_nodes = database.read().split("\n")[:-1]
        database.close()
        return public_nodes

    @staticmethod
    async def get_nonce(diff: str, target: str, URL: str, timeout: float) -> str:
        """
        get_nonce:                  Sends a POST request and returns response.
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

        return requests.post(URL, headers=headers, json=data, timeout=timeout).text

    @staticmethod
    async def find_nonce(diff: str, target: str, nodes: list, timeout: float) -> dict:
        """
        find_nonce:                 Finds and returns the fastest response
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
                asyncio.create_task(SERV.get_nonce(diff, target, node, timeout))
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


if __name__ == "__main__":
    pass
