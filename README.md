#  Password Cracker (Brute-force & Dictionary Attack)

A lightweight Python tool that demonstrates how attackers can attempt to crack **MD5** and **SHA1** hashes.  
It supports both **dictionary-based attacks** (using wordlists) and **brute-force attacks** (character combinations).  
 This project is for **educational and cybersecurity learning purposes only**.  

---

## Installation
```bash
# Clone this repository
git clone https://github.com/YourUsername/PasswordCracker.git

# Navigate into the folder
cd PasswordCracker

# Install dependencies (optional, standard libraries only)
        pip install -r requirements.txt
 Usage

   Dictionary Attack:
      python cracker.py --mode dict --hash 5d41402abc4b2a76b9719d911017c592 --algo md5 --wordlist wordlist.txt
   Brute-force Attack:
      python cracker.py --mode brute --hash 5d41402abc4b2a76b9719d911017c592 --algo md5 --max 5

Example:
  Hash: MD5("hello") → 5d41402abc4b2a76b9719d911017c592

  Run:
   python cracker.py --mode brute --hash 5d41402abc4b2a76b9719d911017c592 --algo md5 --max 5
  Output:
[+] Password found: hello
 Features
✔️ Supports MD5 and SHA1
✔️ Dictionary attack with custom wordlists
✔️ Brute-force with configurable max length
✔️ Lightweight – only uses Python standard libraries

 License
This project is licensed for educational use only.
Please use it responsibly in a controlled environment.

----------------------------------------------------------------------------------------------------------
