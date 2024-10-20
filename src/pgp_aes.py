#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# MY_PGP
# File description:
# PGP-AES
#

from src.utils import *
from src.aes.aes import *
from src.rsa import rsa

def encrypt_pgp_aes(message, key, block_mode, left, right) -> str:
    try:
        aes_key, rsa_key = key.split(":")
        new_left, new_right = rsa_key.split("-")
        encrypted_key = rsa(aes_key, rsa_key, True, False, new_left, new_right)
        encrypted_message = aes(message, aes_key, True, block_mode, "", "")
    except Exception as e:
        print(e)
        exit(84)
    return encrypted_key + "\n" + encrypted_message

def decrypt_pgp_aes(message, key, block_mode, left, right) -> str:
    try:
        aes_key, rsa_key  = key.split(":")
        new_left, new_right = rsa_key.split("-")
        decrypted_key = string_to_hex(rsa(aes_key, rsa_key, False, block_mode, new_left, new_right).split("\n")[0])
        decrypted_message = aes(message, decrypted_key, False, block_mode, "", "")
    except Exception as e:
        print(e)
        exit(84)
    return decrypted_message

def pgp_aes(message, key, encrypt, block_mode, left, right) -> str:
    if encrypt:
        return encrypt_pgp_aes(message, key, block_mode, left, right)
    else:
        return decrypt_pgp_aes(message, key, block_mode, left, right)
