#!/usr/bin/python3
from src.utils import *

def xor_encrypt_decrypt(message, key) -> bytes:
    key_repeated = bytearray()
    key_length = len(key)
    message_length = len(message)
    result = bytes()

    for i in range(message_length):
        key_repeated.append(key[i % key_length])
    for i in range(message_length):
        result += bytes([message[i] ^ key_repeated[i]])
    return result

def pad_message(message, block_size) -> bytes:
    padding_needed = block_size - (len(message) % block_size)
    if padding_needed != block_size:
        message += b'\x00' * padding_needed
    return message

def xor(message: str, key: str, encrypt: bool, block_mode: bool) -> str:
    key_bytes = hex_to_bytes(key)

    message_bytes = hex_to_bytes(string_to_hex(message)) if encrypt else hex_to_bytes(message)

    if (encrypt):
        message_bytes = little_endian(message_bytes)

    if encrypt and not block_mode:
        message_bytes = pad_message(message_bytes, len(key_bytes))

    result_bytes = xor_encrypt_decrypt(message_bytes, key_bytes)

    if (not encrypt):
        result_bytes = little_endian(result_bytes)

    return bytes_to_hex(result_bytes) if encrypt else result_bytes.decode(errors='ignore').rstrip('\x00')
