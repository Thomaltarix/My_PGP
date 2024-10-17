#!/usr/bin/python3
import binascii

def pad_message(message, block_size) -> bytes:
    padding_needed = block_size - (len(message) % block_size)
    if padding_needed != block_size:
        message += b'\x00' * padding_needed
    return message

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

def hex_to_int(hex_str) -> int:
    return int(hex_str, 16)

def int_to_hex(int_str) -> str:
    return hex(int_str)

def int_to_bytes(int_str) -> bytes:
    return int_str.to_bytes((int_str.bit_length() + 7) // 8, 'big')

def bytes_to_int(byte_data) -> int:
    return int.from_bytes(byte_data, 'big')

def bytes_to_string(byte_data) -> str:
    return byte_data.decode(errors='ignore')

def isHex(str):
    try:
        x = hex_to_int(str)
    except:
        return False
    return True
