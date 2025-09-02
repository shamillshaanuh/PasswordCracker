#!/usr/bin/env python3
import hashlib
import itertools
import string
import argparse
import sys
import time

# Supported algorithms
SUPPORTED_ALGOS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
}

# Function to hash a word using chosen algorithm
def hash_word(word, algo="md5"):
    word = word.encode('utf-8')
    if algo not in SUPPORTED_ALGOS:
        raise ValueError(f"Unsupported algorithm: {algo}")
    return SUPPORTED_ALGOS[algo](word).hexdigest()

# Dictionary attack
def dictionary_attack(hash_to_crack, wordlist, algo="md5"):
    print(f"[+] Starting Dictionary Attack with {algo.upper()}...")
    with open(wordlist, 'r', errors='ignore') as f:
        for line in f:
            word = line.strip()
            if hash_word(word, algo) == hash_to_crack:
                print(f"[+] Password found: {word}")
                return word
    print("[-] Password not found in wordlist.")
    return None

# Brute-force attack
def brute_force_attack(hash_to_crack, max_length=4, algo="md5", charset="lower+digits"):
    print(f"[+] Starting Brute-force Attack with {algo.upper()}...")

    # Define charsets
    charset_map = {
        "lower": string.ascii_lowercase,
        "upper": string.ascii_uppercase,
        "digits": string.digits,
        "symbols": string.punctuation,
    }

    # Build charset from user input
    chars = ""
    for part in charset.split(","):
        part = part.strip()
        if part in charset_map:
            chars += charset_map[part]
    if not chars:
        chars = string.ascii_lowercase + string.digits  # default

    print(f"[+] Using charset: {chars}")

    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            word = ''.join(attempt)
            attempts += 1

            if hash_word(word, algo) == hash_to_crack:
                elapsed = time.time() - start_time
                print(f"[+] Password found: {word}")
                print(f"[i] Attempts: {attempts}, Time taken: {elapsed:.2f} sec")
                return word

            # Print progress every 50k attempts
            if attempts % 50000 == 0:
                elapsed = time.time() - start_time
                print(f"[i] Tried {attempts} attempts in {elapsed:.2f} sec...")

    print("[-] Password not found with brute-force.")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Professional Password Cracker (Dictionary / Brute-force)")
    parser.add_argument("--mode", choices=["dict", "brute"], required=True, help="Attack mode")
    parser.add_argument("--hash", required=True, help="Target hash to crack")
    parser.add_argument("--algo", choices=list(SUPPORTED_ALGOS.keys()), default="md5", help="Hashing algorithm")
    parser.add_argument("--wordlist", help="Path to wordlist (for dictionary mode)")
    parser.add_argument("--max", type=int, default=4, help="Max length for brute force")
    parser.add_argument("--charset", default="lower,digits", help="Charsets to use (options: lower, upper, digits, symbols, comma separated)")

    args = parser.parse_args()

    if args.mode == "dict":
        if not args.wordlist:
            print("[-] Please provide a wordlist with --wordlist")
            sys.exit(1)
        dictionary_attack(args.hash, args.wordlist, args.algo)

    elif args.mode == "brute":
        brute_force_attack(args.hash, args.max, args.algo, args.charset)
