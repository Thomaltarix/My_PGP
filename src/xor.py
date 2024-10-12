#!/usr/bin/python3
import binascii
import sys

def hex_to_string(hex_str) -> str:
    """
    Convert a hexadecimal string to a regular string.
    """
    return bytes.fromhex(hex_str).decode(errors='ignore')

def string_to_hex(string) -> str:
    """
    Convert a regular string to a hexadecimal string.
    """
    return string.encode().hex()

def hex_to_bytes(hex_str) -> bytes:
    """
    Convert a hexadecimal string to a byte array.
    """
    return bytes.fromhex(hex_str)

def bytes_to_hex(byte_data) -> str:
    """
    Convert a byte array to a hexadecimal string.
    """
    return binascii.hexlify(byte_data).decode()

def xor_encrypt_decrypt(message, key) -> bytes:
    """
    Perform XOR encryption/decryption on the message with the key.
    """
    # Ensure key length matches message length by repeating the key if needed
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
    """
    Pad the message to make it a multiple of the block size with zeros if necessary.
    """
    padding_needed = block_size - (len(message) % block_size)
    if padding_needed != block_size:
        message += b'\x00' * padding_needed
    return message

def parse_input(option, message):
    hex_message = "596f75206b6e6f77206e6f7468696e672c204a6f6e20536e6f77"  # "You know nothing, Jon Snow"
    hex_key = "576861742069732064656164206d6179206e6576657220646965"  # Some random key

    # Convert hex to bytes
    message_bytes = hex_to_bytes(hex_message)
    key_bytes = hex_to_bytes(hex_key)

    # Pad message to match key length if necessary (stream mode)
    message_bytes_padded = pad_message(message_bytes, len(key_bytes))

    # XOR Encrypt the message
    ciphered_bytes = xor_encrypt_decrypt(message_bytes_padded, key_bytes)
    ciphered_hex = bytes_to_hex(ciphered_bytes)

    print("Ciphered (Hex):", ciphered_hex)

    # XOR Decrypt the message (ciphered data XOR key = original message)
    decrypted_bytes = xor_encrypt_decrypt(ciphered_bytes, key_bytes)
    decrypted_message = decrypted_bytes.decode(errors='ignore').rstrip('\x00')  # Remove padding

    print("Decrypted message:", decrypted_message)

def main():
    #parse_input(sys.argv[1], sys.argv[2])
    print("The message: \"You know nothing, Jon Snow\" is encrypted into: ")
    print(string_to_hex("You know nothing, Jon Snow"))
    """hex_message = "596f75206b6e6f77206e6f7468696e672c204a6f6e20536e6f77"  # "You know nothing, Jon Snow"
    hex_key = "576861742069732064656164206d6179206e6576657220646965"  # Some random key

    # Convert hex to bytes
    message_bytes = hex_to_bytes(hex_message)
    key_bytes = hex_to_bytes(hex_key)

    # Pad message to match key length if necessary (stream mode)
    message_bytes_padded = pad_message(message_bytes, len(key_bytes))

    # XOR Encrypt the message
    ciphered_bytes = xor_encrypt_decrypt(message_bytes_padded, key_bytes)
    ciphered_hex = bytes_to_hex(ciphered_bytes)

    print("Ciphered (Hex):", ciphered_hex)

    # XOR Decrypt the message (ciphered data XOR key = original message)
    decrypted_bytes = xor_encrypt_decrypt(ciphered_bytes, key_bytes)
    decrypted_message = decrypted_bytes.decode(errors='ignore').rstrip('\x00')  # Remove padding

    print("Decrypted message:", decrypted_message)"""

if __name__ == '__main__':
    main()
