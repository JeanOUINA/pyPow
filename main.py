#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  main.py Author "epy3" Date 18.07.2022
from addr.addr import ADDR
from pow.pow import POW
from hashlib import blake2b


def main():
    bd = "67108863"
    n = 1
    data = bytearray([1]);

    hash = blake2b(digest_size=32)
    hash.update(data)
    print(hash.hexdigest())


if __name__ == "__main__":
    main()

## func TestGetPowNonce(t *testing.T) {
## 	bd, _ := new(big.Int).SetString("67108863", 10)
## 	N := 1
## 	data := crypto.Hash256([]byte{1})
## 	timeList := make([]int64, N)
## 	for i := 0; i < N; i++ {
## 		startTime := time.Now()
## 		nonce, _ := pow.GetPowNonce(bd, types.DataHash([]byte{1}))
## 		assert.True(t, pow.CheckPowNonce(bd, nonce, data))
## 		d := time.Now().Sub(startTime).Nanoseconds()
## 		fmt.Println("#", i, ":", d/1e6, "ms", "nonce", nonce)
## 		timeList[i] = d
## 	}
## 
## 	max, min, timeSum, average, std := statistics(timeList)
## 	fmt.Println("average", average/1e6, "ms max", max/1e6, "ms min", min/1e6, "sum", timeSum/1e6, "standard deviation", std)
## }
