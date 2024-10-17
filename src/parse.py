#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# MY_PGP
# File description:
# Parse
#
import sys
from src.utils import *

class pgpArgs():
    def __init__(self):
        self.valid_systems = ["xor", "aes", "rsa", "pgp-xor", "pgp-aes"]
        self.fail = False
        self.crypto_system = None
        self.mode = None
        self.block_mode = None
        self.KEY = None
        self.g1 = None
        self.g2 = None
        self.key_bytes = None
        self.message_bytes = None
        if not self.parseArgs():
            self.fail = True

    def check_message_encoding(self, message):
        encrypt = self.mode == "-c"
        try:
            self.message_bytes = hex_to_bytes(string_to_hex(message)) if encrypt else hex_to_bytes(message)
        except:
            return False
        return True

    def check_key_encoding(self):
        try:
            if not self.crypto_system == "rsa":
                self.key_bytes = hex_to_bytes(self.KEY)
            else:
                self.key_bytes = self.KEY
        except:
            self.fail = True

    def parseArgs(self):
        if len(sys.argv) < 3:
            print("Lack of arguments given.", file=sys.stderr)
            return False
        self.crypto_system = sys.argv[1]
        if self.crypto_system not in self.valid_systems:
            print("Invalid crypto system.", file=sys.stderr)
            return False
        self.mode = sys.argv[2]
        if self.mode != "-c" and self.mode != "-d" and self.mode != "-g":
            print("Invalid mode.", file=sys.stderr)
            return False
        if self.mode == "-g" and (len(sys.argv) < 5 or self.crypto_system != "rsa"):
            print("-g issue.", file=sys.stderr)
            return False
        # if (self.mode != "-g"):
        #     self.MESSAGE = input("")
        #     if (not self.MESSAGE):
        #         print("No message given.")
        #         return False
        if self.mode == "-g":
            self.g1 = sys.argv[3]
            self.g2 = sys.argv[4]
            if (not isHex(self.g1) or not isHex(self.g2)):
                print("Invalid hex string.", file=sys.stderr)
                return False
        if self.mode == "-c" or self.mode == "-d":
            if len(sys.argv) < 4:
                print("No key given.", file=sys.stderr)
                return False
        if sys.argv[3] == "-b":
            self.block_mode = True
            if self.crypto_system == "rsa":
                print("Invalid option.", file=sys.stderr)
                return False
        if self.mode != "-g":
            self.KEY = sys.argv[4] if self.block_mode else sys.argv[3]
            self.check_key_encoding()
        return True

    def displayArgs(self):
        print("crypto_system: ", self.crypto_system)
        print("mode: ", self.mode)
        print("block_mode: ", self.block_mode)
        print("key: ", self.KEY)
        print("fail: ", self.fail)
        print("G1: ", self.g1)
        print("G2: ", self.g2)
