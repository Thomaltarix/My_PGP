#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# MY_PGP
# File description:
# Help
#

def display_help():
    help_text = """
USAGE
    ./my_pgp crypto_system mode [OPTIONS] [key]

DESCRIPTION
    The MESSAGE is read from standard input.

    crypto_system
        "xor"       computation using XOR algorithm
        "aes"       computation using 128-bit AES algorithm
        "rsa"       computation using RSA algorithm
        "pgp-xor"   computation using both RSA and XOR algorithm
        "pgp-aes"   computation using both RSA and 128-bit AES algorithm

    mode
        -c          MESSAGE is clear and we want to cipher it
        -d          MESSAGE is ciphered and we want to decipher it
        -g P Q      for RSA only: Don't read a MESSAGE, but instead generate a public and
                    private key pair from the prime number P and Q

    OPTIONS
        -b          for XOR, AES, and PGP, only works on one block. The MESSAGE and the
                    symmetric key must be the same size

    key             Key used to cipher/decipher MESSAGE (incompatible with -g mode)
    """
    print(help_text)
    return 0
