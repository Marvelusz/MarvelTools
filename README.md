# MARVELUS v1.0

Open Source Intelligence (OSINT) Framework written in Python.

## Features

- 🔍 Username Lookup (Sherlock)
- 📧 Email Lookup (Holehe)
- 👤 Username Enumeration (Maigret)
- 📱 Phone Number Lookup (NumVerify API)
- 🌐 Address Lookup
- 📍 Coordinate Lookup
- 🔓 Port Scanner (Nmap)

---

# 📦 Installation

> *⚠️ Before You Start*
>
> This framework uses the *NumVerify API* for Phone Number Lookup.
>
> Before running the framework, create a file named *.env* in the project root (same folder as main.py) and add:
>
> env
> NUMVERIFY_API_KEY=YOUR_API_KEY
> 
>
> Replace YOUR_API_KEY with your own NumVerify API key.

---

## 🪟 Windows

### Clone Repository
bash
git clone https://github.com/Marvelusz/MarvelTools.git
cd MarvelTools


### (Optional) Create Virtual Environment
bash
python -m venv venv
venv\Scripts\activate


### Install Dependencies
bash
pip install -r requirements.txt


### Run
bash
python main.py


---

## 🐧 Linux / Ubuntu / WSL

### Update System
bash
sudo apt update && sudo apt upgrade -y


### Install Python & Git
bash
sudo apt install python3 python3-pip python3-venv git -y


### Clone Repository
bash
git clone https://github.com/Marvelusz/MarvelTools.git
cd MarvelTools


### Create Virtual Environment
bash
python3 -m venv venv
source venv/bin/activate


### Install Dependencies
bash
pip3 install -r requirements.txt


### Run
bash
python3 main.py


---

## 📱 Termux (Android)

### Update Packages
bash
pkg update && pkg upgrade -y


### Install Dependencies
bash
pkg install python git clang -y


### Clone Repository
bash
git clone https://github.com/Marvelusz/MarvelTools.git
cd MarvelTools


### Install Python Packages
bash
pip install -r requirements.txt


### Run
bash
python main.py