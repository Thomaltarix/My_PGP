#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# MY_PGP
# File description:
# Main
#
from src.help import display_help
from src.parse import pgpArgs
from src.xor import xor
from src.utils import *
import sys




def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        return display_help()
    args = pgpArgs()
    # args.displayArgs()
    if (args.fail):
        return 84
    algo = xor if (args.CRYPTO_SYSTEM == "xor") else xor
    if (args.OPT_b):
        message = input("")
        message_bytes = hex_to_bytes(string_to_hex(message)) if (args.MODE == "-c") else hex_to_bytes(message)
        if len(message_bytes) != len(hex_to_bytes(args.KEY)):
            print("Block mode enabled. Key length must be equal to message length.", file=sys.stderr)
            return 84
        else:
            print(algo(message, args.KEY, args.MODE == '-c', args.OPT_b))
    else:
        while True:
            data = sys.stdin.read(len(hex_to_bytes(args.KEY)))
            if not data:
                break
            print(algo(data, args.KEY, args.MODE == '-c', args.OPT_b))
    return 0

if __name__ == "__main__":
    sys.exit(main())
