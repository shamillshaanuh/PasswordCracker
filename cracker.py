import hashlib
import itertools
import string
import argparse


# Function to hash a word using chosen algorithm
def hash_word(word, algo="md5"):
word = word.encode('utf-8')
if algo == "md5":
return hashlib.md5(word).hexdigest()
elif algo == "sha1":
return hashlib.sha1(word).hexdigest()
else:
raise ValueError("Unsupported algorithm: choose 'md5' or 'sha1'")


# Dictionary attack
def dictionary_attack(hash_to_crack, wordlist, algo="md5"):
print("[+] Starting Dictionary Attack...")
with open(wordlist, 'r', errors='ignore') as f:
for line in f:
word = line.strip()
if hash_word(word, algo) == hash_to_crack:
print(f"[+] Password found: {word}")
return word
print("[-] Password not found in wordlist.")
return None


# Brute-force attack
def brute_force_attack(hash_to_crack, max_length=4, algo="md5"):
print("[+] Starting Brute-force Attack...")
chars = string.ascii_lowercase + string.digits # now includes numbers
for length in range(1, max_length + 1):
for attempt in itertools.product(chars, repeat=length):
word = ''.join(attempt)
if hash_word(word, algo) == hash_to_crack:
print(f"[+] Password found: {word}")
return word
print("[-] Password not found with brute-force.")
return None


if __name__ == "__main__":
parser = argparse.ArgumentParser(description="Password Cracker (Dictionary / Brute-force)")
parser.add_argument("--mode", choices=["dict", "brute"], required=True, help="Attack mode")
parser.add_argument("--hash", required=True, help="Target hash to crack")
parser.add_argument("--algo", choices=["md5", "sha1"], default="md5", help="Hashing algorithm")
parser.add_argument("--wordlist", help="Path to wordlist (for dictionary mode)")
parser.add_argument("--max", type=int, default=4, help="Max length for brute force")


args = parser.parse_args()


if args.mode == "dict":
if not args.wordlist:
print("[-] Please provide a wordlist with --wordlist")
else:
dictionary_attack(args.hash, args.wordlist, args.algo)


elif args.mode == "brute":
brute_force_attack(args.hash, args.max, args.algo)
