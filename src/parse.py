#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# MY_PGP
# File description:
# Parse
#
import sys

class pgpArgs():
    def __init__(self):
        self.valid_systems = ["xor", "aes", "rsa", "pgp-xor", "pgp-aes"]
        self.fail = False
        self.CRYPTO_SYSTEM = None
        self.MODE = None
        self.OPT_b = None
        self.KEY = None
        self.g1 = None
        self.g2 = None
        if (not self.parseArgs()):
            self.fail = True

    def parseArgs(self):
        if (len(sys.argv) < 3):
            print("Lack of arguments given.", file=sys.stderr)
            return False
        self.CRYPTO_SYSTEM = sys.argv[1]
        if (self.CRYPTO_SYSTEM not in self.valid_systems):
            print("Invalid crypto system.", file=sys.stderr)
            return False
        self.MODE = sys.argv[2]
        if (self.MODE != "-c" and self.MODE != "-d" and self.MODE != "-g"):
            print("Invalid mode.", file=sys.stderr)
            return False
        if (self.MODE == "-g" and (len(sys.argv) < 5 or self.CRYPTO_SYSTEM != "rsa")):
            print("-g issue.", file=sys.stderr)
            return False
        # if (self.MODE != "-g"):
        #     self.MESSAGE = input("")
        #     if (not self.MESSAGE):
        #         print("No message given.")
        #         return False
        if (self.MODE == "-g"):
            self.g1 = sys.argv[3]
            self.g2 = sys.argv[4]
        if (self.MODE == "-c" or self.MODE == "-d"):
            if len(sys.argv) < 4:
                print("No key given.", file=sys.stderr)
                return False
        if (sys.argv[3] == "-b"):
            self.OPT_b = True
            if (self.CRYPTO_SYSTEM == "rsa"):
                print("Invalid option.", file=sys.stderr)
                return False
        if (self.MODE != "-g"):
            self.KEY = sys.argv[4] if (self.OPT_b) else sys.argv[3]
        return True

    def displayArgs(self):
        print("CRYPTO_SYSTEM: ", self.CRYPTO_SYSTEM)
        print("MODE: ", self.MODE)
        print("OPT_b: ", self.OPT_b)
        print("KEY: ", self.KEY)
        print("MESSAGE: ", self.MESSAGE)
        print("FAIL: ", self.fail)
        print("G1: ", self.g1)
        print("G2: ", self.g2)
