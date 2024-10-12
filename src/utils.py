#!/usr/bin/python3
import binascii


def hex_to_string(hex_str) -> str:
    return bytes.fromhex(hex_str).decode(errors='ignore')

def string_to_hex(string) -> str:
    return string.encode().hex()

def hex_to_bytes(hex_str) -> bytes:
    return bytes.fromhex(hex_str)

def bytes_to_hex(byte_data) -> str:
    return binascii.hexlify(byte_data).decode()

def little_endian(data : bytes) -> bytes:
    return data[::-1]
