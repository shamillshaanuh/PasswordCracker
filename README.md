#  PasswordCracker - Hash Cracking Tool
**Author:** MUHAMMED SHAMIL

A simple yet effective password cracking tool for educational and authorized security testing only.

---

##  Overview
PasswordCracker is a lightweight Python-based hash cracking tool.  
It supports multiple cracking modes such as **Brute-Force** and **Dictionary Attack**, making it useful for security students and penetration testers who want to understand how password cracking works.

---

##  Features
- Supports multiple hashing algorithms (MD5, SHA1, SHA256, etc.)
- Two cracking modes:
  - **Brute-Force Attack** (tries all possible character combinations up to a given length)
  - **Dictionary Attack** (uses a custom wordlist)
- Adjustable character sets and maximum length for brute-force
- Works on Linux, macOS, and Windows
- Easy to extend for new algorithms and modes

---

##  Installation

### 1. Clone the Repository
```bash
git clone https://github.com/shamillshaanuh/PasswordCracker.git
cd PasswordCracker
```
### 2. Install Dependencies

PasswordCracker requires Python. 
If not already installed, install Python3:
```
sudo apt update
sudo apt install python3 python3-pip -y
```
### Usage Guide

Use a wordlist file to crack a hash:
```
python3 cracker.py --mode dict --hash --algo md5 --wordlist /path
```
### Example Output
```
[*] Starting brute-force attack...
[+] Hash matched! Password found: ......
```
## Disclaimer

This tool is developed strictly for educational purposes and authorized penetration testing.
The author is not responsible for any misuse or illegal activity.
