from src.aes.data import *

def RotWord(word):
    return word[1:] + word[:1]

def addRoundKey(word1,word2):
    return [word1[i] ^ word2[i] for i in range(0, len(word1))]

def printLine(line):
    print(f"{line[0]:x} {line[0+1]:x} {line[0+2]:x} {line[0+3]:x}")

def printTab(keymatrix):
    for i in range(0, len(keymatrix), 4):
            print(f"{keymatrix[i]:x} {keymatrix[i+1]:x} {keymatrix[i+2]:x} {keymatrix[i+3]:x}")

def InvSubBytes(word):
    return [invSBOX[i] for i in word]

def SubBytes(currentCol):
    return [sbox[i] for i in currentCol]
