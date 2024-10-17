from ast import List

def ShiftRows(word):
    new = list(word)
    new[1] = word[5]
    new[5] = word[9]
    new[9] = word[13]
    new[13] = word[1]

    new[2] = word[10]
    new[6] = word[14]
    new[10] = word[2]
    new[14] = word[6]

    new[3] = word[15]
    new[7] = word[3]
    new[11] = word[7]
    new[15] = word[11]

    return new

def InvShiftRows(word):
    new = list(word)
    new[1] = word[13]
    new[5] = word[1]
    new[9] = word[5]
    new[13] = word[9]

    new[2] = word[10]
    new[6] = word[14]
    new[10] = word[2]
    new[14] = word[6]

    new[3] = word[7]
    new[7] = word[11]
    new[11] = word[15]
    new[15] = word[3]

    return new
