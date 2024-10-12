#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# MY_PGP
# File description:
# Main
#
from src.help import display_help
from src.parse import pgpArgs
import sys



def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        return display_help()
    args = pgpArgs()
    # args.displayArgs()
    if (args.fail):
        return 84
    return 0

if __name__ == "__main__":
    sys.exit(main())
