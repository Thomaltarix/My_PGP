from src.aes.data import *
from src.aes.ShiftRows import *
from src.aes.MixColumns import *
from src.aes.KeyExpansion import *
from src.aes.utils import *
from src.utils import *


def aes_decrypt(message, keyExpanded):
    keyExpanded = rev_expandedkey(keyExpanded)
    message = addRoundKey(message, keyExpanded[:16])
    keyExpanded = keyExpanded[16:]

    message = InvShiftRows(message)
    message = InvSubBytes(message)

    for i in range(0,9):
        message = addRoundKey(message, keyExpanded[0:16])
        keyExpanded = keyExpanded[16:]
        mixIt(message, invMixColmn)
        message = InvShiftRows(message)
        message = InvSubBytes(message)

    message = addRoundKey(message, keyExpanded[0:16])
    keyExpanded = keyExpanded[16:]

    return message


def aes_crypt(message, keyExpanded):

    message = addRoundKey(message, keyExpanded[0:16])
    keyExpanded = keyExpanded[16:]

    for i in range(0, 9):
        message = SubBytes(message)

        message = ShiftRows(message)

        mixIt(message, mixColmn)

        message = addRoundKey(message, keyExpanded[0:16])
        keyExpanded = keyExpanded[16:]

    message = SubBytes(message)
    message = ShiftRows(message)
    message = addRoundKey(message, keyExpanded[0:16])
    keyExpanded = keyExpanded[16:]

    return message

def swap32(content):
    content = list(content)
    for i in range(0, len(content), 4):
        line = content[i:i+4]
        content[i:i+4] = line[::-1]
    return content

def aes(message: str, key: str, encrypt: bool, block_mode: bool, left, right) -> str:
    key_bytes = list(hex_to_bytes(key))
    message_bytes = list(hex_to_bytes(string_to_hex(message)) if encrypt else list(hex_to_bytes(message)))

    if not block_mode and (len(message_bytes) != len(key_bytes)):
        message_bytes = pad_message(message_bytes, len(key_bytes))

    if encrypt:
        key_bytes = swap32(key_bytes)
    else:
        message_bytes = swap32(message_bytes)
        key_bytes = swap32(key_bytes)

    keyExpanded = keyExpansion(key_bytes)

    message = aes_crypt(message_bytes, keyExpanded) if encrypt else aes_decrypt(message_bytes, keyExpanded)
    if encrypt:
        message = swap32(message)
    return bytes_to_hex(bytes(message)) if encrypt else bytes(message).decode(errors='ignore')
