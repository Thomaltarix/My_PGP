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
    aes_key, rsa_key = key.split(":")
    new_left, new_right = rsa_key.split("-")
    encrypted_message = aes(message, aes_key, True, block_mode, "", "")
    encrypted_key = rsa(aes_key, rsa_key, True, block_mode, new_left, new_right)
    return encrypted_key + "\n" + encrypted_message

def decrypt_pgp_aes(message, key, block_mode, left, right) -> str:
    xor_key, rsa_key  = key.split(":")
    new_left, new_right = rsa_key.split("-")
    decrypted_key = rsa(xor_key, rsa_key, False, block_mode, new_left, new_right)
    decrypted_message = aes(message, decrypted_key, False, block_mode, "", "")
    return decrypted_message

def pgp_aes(message, key, encrypt, block_mode, left, right) -> str:
    if encrypt:
        return encrypt_pgp_aes(message, key, block_mode, left, right)
    else:
        return decrypt_pgp_aes(message, key, block_mode, left, right)
