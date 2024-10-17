from src.aes.data import *
from src.aes.ShiftRows import *
from src.aes.MixColumns import *
from src.aes.KeyExpansion import *
from src.aes.utils import *


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



#und, plug, rev. optiEstheALL
