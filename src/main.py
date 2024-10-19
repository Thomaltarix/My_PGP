#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# MY_PGP
# File description:
# Main
#
import src.rsa
from src.help import display_help
from src.parse import pgpArgs
from src.xor import xor
from src.rsa import rsa
from src.pgp_xor import pgp_xor
from src.utils import *
from src.aes.aes import *
import sys

def block_mode(args, algo):
    key = args.KEY
    if algo == pgp_xor:
        key = args.KEY.split(":")[0]
    message = sys.stdin.read(len(hex_to_bytes(key)) * (2 if args.mode == "-d" else 1)).strip()
    if not args.check_message_encoding(message):
        print("Invalid message encoding.", file=sys.stderr)
        return 84
    message_bytes = hex_to_bytes(string_to_hex(message)) if (args.mode == "-c") else hex_to_bytes(message)

    if len(message_bytes) != len(hex_to_bytes(key)) and not args.crypto_system == "pgp-xor":
        print("Block mode enabled. Key length must == message length.", file=sys.stderr)
        return 84
    else:
        if args.crypto_system == "pgp-xor":
            print(algo(message, args.KEY, args.mode == '-c', args.block_mode, args.left, args.right))
        else:
            print(algo(message, key, args.mode == '-c', args.block_mode, args.left, args.right))
    return 0

def stream_mode(args, algo):
    while True:
        key = args.KEY
        if algo == rsa:
            data = sys.stdin.read().strip()
        else:
            if algo == pgp_xor:
                key = args.KEY.split(":")[0]
            data = sys.stdin.read(len(hex_to_bytes(key)) * (2 if args.mode == "-d" else 1)).strip()
        if not data:
            break
        if not args.check_message_encoding(data):
            print("Invalid message encoding.", file=sys.stderr)
            return 84
        print(algo(data, args.KEY, args.mode == '-c', args.block_mode, args.left, args.right))
    return 0

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        return display_help()
    args = pgpArgs()
    if args.fail:
        return 84
    if args.crypto_system == "xor":
        algo = xor
    elif args.crypto_system == "rsa":
        algo = rsa
    elif args.crypto_system == "aes":
        algo = aes
    elif args.crypto_system == "pgp-xor":
        algo = pgp_xor
    else:
        algo = None
    if algo is None:
        print("We currently dont manage this algo.", file=sys.stderr)
        return 0
    if args.mode == "-g":
        return src.rsa.generateKeys(args.g1, args.g2)
    if args.block_mode:
        if block_mode(args, algo) != 0:
            return 84
    else:
        if stream_mode(args, algo) != 0:
            return 84
    return 0

if __name__ == "__main__":
    sys.exit(main())
