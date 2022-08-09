#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  pow_test.py Author "epy3" Date 18.07.2022

from hashlib import blake2b
from pow import POW
import pytest


""" NOTE: Some test can fail due to randomness. """


def test_difficulty_to_target_true():
    difficulty = 67108863
    target = 115792087511879608725930038149998942284013621552863320996860945217282073690112  ##
    assert POW.target_to_difficulty(target) == difficulty


def test_difficulty_to_target_false():
    difficulty = 67108864
    target = 215792087511879608725930038149998942284013621552863320996860945217282073690112  ##
    assert POW.target_to_difficulty(target) != difficulty


def test_hash_with_c():
    threshold = int(0xFFFFFFC000000000)
    array = threshold.to_bytes(8, "little")
    hasher = blake2b(digest_size=32)
    hasher.update(array)
    assert (
        hasher.hexdigest()
        == "ce19a171683a98f147a2a6480bfb9446954ec7a4e143ddfb2d4cdf72f0316553"
    )


def test_hash256():
    hasher = blake2b(digest_size=32)
    hasher.update(bytearray([1, 2, 1, 3]))
    ret1 = hasher.hexdigest()

    hasher2 = blake2b(digest_size=32)
    hasher2.update(bytearray([1, 2]))
    hasher2.update(bytearray([1, 3]))
    assert ret1 == hasher2.hexdigest()


def test_quick_inc():
    arr1_in = bytearray([1, 2])
    arr1_res = bytearray([1, 3])
    assert POW.quick_inc(arr1_in) == arr1_res


def test_quick_inc_1():
    arr2_in = bytearray([1, 0xFF])
    arr2_res = bytearray([2, 0])
    assert POW.quick_inc(arr2_in) == arr2_res


def test_quick_inc_2():
    arr3_in = bytearray([0xFF, 0xFF])
    arr3_res = bytearray([0, 0])
    assert POW.quick_inc(arr3_in) == arr3_res


def test_quick_inc_3():
    arr4_in = bytearray([1, 0xFF, 0xFF, 0xFF])
    arr4_res = bytearray([2, 0, 0, 0])
    assert POW.quick_inc(arr4_in) == arr4_res


def test_quick_greater():
    byte_x = "FF3031"
    byte_y = "003032"
    byte_x = bytearray.fromhex(byte_x)
    byte_y = bytearray.fromhex(byte_y)

    byte_x = "FF3031"
    byte_y = "FF3031"
    byte_x = bytearray.fromhex(byte_x)
    byte_y = bytearray.fromhex(byte_y)

    assert POW.quick_greater(byte_x, byte_y, len(byte_x)) == False


def test_check_pow_nonce():
    nonce = bytearray.fromhex("96dcde7641923e2a")
    nonce.reverse()

    data = "718CC2121C3E641059BC1C2CFC45666C718CC2121C3E641059BC1C2CFC45666C"
    data = bytearray.fromhex(data)

    d = 67108863

    assert POW.check_pow_nonce(d, nonce, data) == True


def test_check_pow_nonce_false():
    nonce = bytearray.fromhex("96dcde7641923e2a")
    nonce.reverse()

    data = "818CC2121C3E641059BC1C2CFC45666C718CC2121C3E641059BC1C2CFC45666C"
    data = bytearray.fromhex(data)

    d = 67108863

    assert POW.check_pow_nonce(d, nonce, data) == False


def test_padding():
    data = POW.pad_to_32bytes(bytearray([1, 2, 3, 4]))
    assert len(data) == 32


def test_get_pow_nonce():
    data = "35c82fe515c2982c5ef75226eab35f3fb14952f8ef59005f02893cd3dca4db09"
    data = bytearray.fromhex(data)

    diff = 300000

    # get nonce
    nonce = POW.get_pow_nonce(diff, data)
    # check nonce
    assert POW.check_pow_nonce(diff, nonce, data)


def test_map_pow_nonce_range():
    data = "35c82fe515c2982c5ef75226eab35f3fb14952f8ef59005f02893cd3dca4db09"
    data = bytearray.fromhex(data)

    diff = 300000

    # get nonce
    nonce = POW.pow_nonce_random_range(diff, data, 1000000)
    # check nonce
    assert POW.check_pow_nonce(diff, nonce, data)


def test_map_pow_nonce_numbers():
    data = "35c82fe515c2982c5ef75226eab35f3fb14952f8ef59005f02893cd3dca4db09"
    data = bytearray.fromhex(data)

    diff = 3000

    # get nonce
    nonce = POW.pow_nonce_num_range(diff, data, 0, 100000)
    # check nonce
    assert POW.check_pow_nonce(diff, nonce, data)


if __name__ == "__main__":
    exit()
