from ast import List
from src.aes.utils import *

def keyExpansion(key : List):
    global rcon

    for i in range(0,10):
        for i in range(0,4):
            newline = key[len(key) - 4: len(key) + 1]
            if (i == 0):
                newline = RotWord(newline)
                newline = SubBytes(newline)
                rConCol = rcon[0:4]
                rcon = rcon[4:]
                newline = addRoundKey(newline, rConCol)
            wL4 = key[len(key) - 16: len(key) - 12]
            newline = addRoundKey(newline, wL4)
            key += newline
    return key



def rev_expandedkey(keyExpanded):
    keys = [keyExpanded[i:i+16] for i in range(0, len(keyExpanded), 16)]
    keys = keys[::-1]
    res = []
    for i in range(len(keys)):
        for k in keys[i]:
            res.append(k)
    return res
