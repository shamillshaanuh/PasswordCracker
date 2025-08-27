# 🔐 Password Cracker (Brute-force & Dictionary Attack)

A simple password cracker written in Python that supports **MD5** and **SHA1** hashes.  
It can crack passwords using **dictionary wordlists** or **brute-force attacks**.

---

## Installation
```bash
# Clone this repository
git clone https://github.com/YourUsername/PasswordCracker.git

# Navigate into the folder
cd PasswordCracker

# Install dependencies (optional, standard libs only)
pip install -r requirements.txt

### Usage
Dictionary Attack
python cracker.py --mode dict --hash 5d41402abc4b2a76b9719d911017c592 --algo md5 --wordlist wordlist.txt

Brute-force Attack
python cracker.py --mode brute --hash 5d41402abc4b2a76b9719d911017c592 --algo md5 --max 5

### Example

MD5("hello") = 5d41402abc4b2a76b9719d911017c592

Run:

python cracker.py --mode brute --hash 5d41402abc4b2a76b9719d911017c592 --algo md5 --max 5


Output:

[+] Password found: hello
