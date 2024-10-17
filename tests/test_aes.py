import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.aes.KeyExpansion import keyExpansion
from src.aes.aes import *



key = [
        0x2b, 0x7e, 0x15,0x16, 0x28,0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c
    ]

message = [
        0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34
    ]



keyExpansion(key)
keyExpandedSave = list(key)

print("tab natural")
# printTab(message)

message_cyphered = aes_crypt(message, key)

print("tab cyphered")
# printTab(message_cyphered)

print("tab uncyphered")
message_decyphered = aes_decrypt(message_cyphered, keyExpandedSave)
# printTab(message_decyphered)


assert(message == message_decyphered)
