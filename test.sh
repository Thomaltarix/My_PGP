#!/bin/bash

# Function to check the exit code and print success or failure
check_exit_code() {
    if [ $? -eq 0 ]; then
        echo "Test $1: SUCCESS"
    else
        echo "Test $1: FAILURE"
        exit 84
    fi
}

# Compilation step
echo "Compiling project with Makefile..."
make re
check_exit_code "Compilation"

# Test XOR encryption and decryption (block mode)
echo "Running XOR tests..."
echo "You know nothing, Jon Snow" > message
./my_pgp xor -c -b 576861742069732064656164206d6179206e6576657220646965 < message > ciphered
check_exit_code "XOR Encryption"
./my_pgp xor -d -b 576861742069732064656164206d6179206e6576657220646965 < ciphered | cat -e
check_exit_code "XOR Decryption"

# Test AES encryption and decryption (block mode)
echo "Running AES tests..."
echo "All men must die" > message
./my_pgp aes -c -b 57696e74657220697320636f6d696e67 < message > ciphered
check_exit_code "AES Encryption"
./my_pgp aes -d -b 57696e74657220697320636f6d696e67 < ciphered | cat -e
check_exit_code "AES Decryption"

# Test RSA key generation and encryption/decryption (small keys)
echo "Running RSA tests..."
./my_pgp rsa -g d3 e3 > keys
check_exit_code "RSA Key Generation"
public_key=$(grep "public key" keys | cut -d ' ' -f 3)
private_key=$(grep "private key" keys | cut -d ' ' -f 3)

echo "WF" | ./my_pgp rsa -c $public_key > ciphered
check_exit_code "RSA Encryption"
cat ciphered | ./my_pgp rsa -d $private_key | cat -e
check_exit_code "RSA Decryption"

# Test Pretty Good Privacy (PGP) encryption and decryption
echo "Running PGP tests..."
echo "The night is dark and full of terrors" > message
./my_pgp pgp-aes -c 57696e74657220697320636f6d696e67 < message > ciphered
check_exit_code "PGP AES Encryption"
./my_pgp pgp-aes -d 57696e74657220697320636f6d696e67 < ciphered | cat -e
check_exit_code "PGP AES Decryption"

# Clean up
echo "Cleaning up..."
make fclean
check_exit_code "Cleaning up"

echo "All tests passed successfully."
exit 0
