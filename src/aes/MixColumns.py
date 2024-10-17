def gal(a, b):
    res = 0
    wrk = 0
    interv = 256
    rangeToSeek = 8

    for i in range(rangeToSeek):
        if b & 1 == 1: res = res ^ a
        wrk = a & 0x80
        a <<= 1
        if wrk == 0x80: a = a ^ 0x1b
        b >>= 1
    return res % interv

def mixColmn(colmn):
    tmp = list(colmn)
    colmn[0] = gal(tmp[0],2) ^ tmp[3] ^ tmp[2] ^ gal(tmp[1],3)
    colmn[1] = gal(tmp[1],2) ^ tmp[0] ^ tmp[3] ^ gal(tmp[2],3)
    colmn[2] = gal(tmp[2],2) ^ tmp[1] ^ tmp[0] ^ gal(tmp[3],3)
    colmn[3] = gal(tmp[3],2) ^ tmp[2] ^ tmp[1] ^ gal(tmp[0],3)

def invMixColmn(colmn):
    tmp = list(colmn)
    colmn[0] = gal(tmp[0], 14) ^ gal(tmp[3], 9) ^ gal(tmp[2], 13) ^ gal(tmp[1], 11)
    colmn[1] = gal(tmp[1], 14) ^ gal(tmp[0], 9) ^ gal(tmp[3], 13) ^ gal(tmp[2], 11)
    colmn[2] = gal(tmp[2], 14) ^ gal(tmp[1], 9) ^ gal(tmp[0], 13) ^ gal(tmp[3], 11)
    colmn[3] = gal(tmp[3], 14) ^ gal(tmp[2], 9) ^ gal(tmp[1], 13) ^ gal(tmp[0], 11)


def mixIt(message, mixFunc):
    for i in range(4):
        line = message[i*4:i*4+4]
        mixFunc(line)
        message[i*4:i*4+4] = line
