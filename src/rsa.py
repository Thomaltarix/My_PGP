#!/usr/bin/python3

from src.utils import *
from math import gcd

def isPrime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def encrypt_rsa(message: str, key: str, left, right) -> str:
    message_bytes = little_endian(hex_to_bytes(string_to_hex(message)))

    n = bytes_to_int(little_endian(hex_to_bytes(right)))
    e = bytes_to_int(little_endian(hex_to_bytes(left)))

    encrypted_message = pow(bytes_to_int(message_bytes), e, n)
    return bytes_to_hex(little_endian(int_to_bytes(encrypted_message)))


def decrypt_rsa(message: str, key: str, left, right) -> str:
    message_bytes = little_endian(hex_to_bytes(message))

    n = bytes_to_int(little_endian(hex_to_bytes(right)))
    d = bytes_to_int(little_endian(hex_to_bytes(left)))

    decrypted_message = pow(bytes_to_int(message_bytes), d, n)
    return bytes_to_string(little_endian(int_to_bytes(decrypted_message)))

def rsa(message: str, key: str, encrypt: bool, block_mode: bool, left, right) -> str:
    if encrypt:
        return encrypt_rsa(message, key, left, right)
    return decrypt_rsa(message, key, left, right)

def getModInverse(e: int, phi: int) -> int:
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

def getMaxFermatPrimeNumber(phi: int) -> int:
    fermat_primes = [3, 5, 17, 257, 65537]
    for prime in fermat_primes[::-1]:
        if phi > prime > 1 == gcd(prime, phi):
            return prime
    return 0
        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def generateKeys(p: str, q:str):
    if not p or not q:
        return "p and q must be provided."
    p = hex_to_int(p)
    q = hex_to_int(q)

    n = new_p * new_q
    phi = (new_p - 1) * (new_q - 1)
    e = getMaxFermatPrimeNumber(phi)
    if gcd(e, phi) != 1 or e == 0:
        return "Error: e and phi aren't coprime, choose different p and q."

    d = getModInverse(e, phi)
    n_little_endian = little_endian(int_to_bytes(n))
    e_little_endian = little_endian(int_to_bytes(e))
    d_little_endian = little_endian(int_to_bytes(d))
    print(f"public key: {str(bytes_to_hex(e_little_endian))}-{str(bytes_to_hex(n_little_endian))}")
    print(f"private key: {str(bytes_to_hex(d_little_endian))}-{str(bytes_to_hex(n_little_endian))}")
    return 0
