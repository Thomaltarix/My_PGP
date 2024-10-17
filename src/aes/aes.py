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

def aes(message: str, key: str, encrypt: bool, block_mode: bool) -> str:
    key_bytes = list(hex_to_bytes(key))
    key_bytes = swap32(key_bytes)

    message_bytes = list(hex_to_bytes(string_to_hex(message)) if encrypt else hex_to_bytes(message))

    if not block_mode and (len(message_bytes) != len(key_bytes)):
        message_bytes = pad_message(message_bytes, len(key_bytes))

    keyExpanded = keyExpansion(key_bytes)

    messageCyphered = aes_crypt(message_bytes, keyExpanded)
    messageCyphered = swap32(messageCyphered)
    return bytes_to_hex(bytes(messageCyphered))

    # # if encrypt:
    # #     message_bytes = little_endian(message_bytes)



    # result_bytes = xor_encrypt_decrypt(message_bytes, key_bytes)

    # # if not encrypt:
    # #     result_bytes = little_endian(result_bytes)
    # return bytes_to_hex(result_bytes) if encrypt else result_bytes.decode(errors='ignore').rstrip('\x00')




#und, plug, rev. optiEstheALL
