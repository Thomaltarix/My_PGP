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
from src.aes.aes import *
from src.utils import *
import sys

def block_mode(args, algo):
    message = input("")
    if not args.check_message_encoding(message):
        print("Invalid message encoding.", file=sys.stderr)
        return 84
    message_bytes = hex_to_bytes(string_to_hex(message)) if (args.mode == "-c") else hex_to_bytes(message)
    if len(message_bytes) != len(hex_to_bytes(args.KEY)):
        print("Block mode enabled. Key length must == message length.", file=sys.stderr)
        return 84
    else:
        print(algo(message, args.KEY, args.mode == '-c', args.block_mode))
    return 0

def stream_mode(args, algo):
    while True:
        data = sys.stdin.read().strip()
        if not data:
            break
        if not args.check_message_encoding(data):
            print("Invalid message encoding.", file=sys.stderr)
            return 84
        print(algo(data, args.KEY, args.mode == '-c', args.block_mode))
    return 0

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        return display_help()
    args = pgpArgs()
    if args.fail:
        return 84
    algo = None
    if args.crypto_system == "xor" : algo = xor
    if args.crypto_system == "aes" : algo = aes
    if (algo == None):
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
