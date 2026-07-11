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

```sh
git clone https://github.com/Marvelusz/MarvelTools.git
```

### Enter Project Directory

```sh
cd MarvelTools
```

### (Optional) Create Virtual Environment

```sh
python -m venv venv
```

### Activate Virtual Environment

```sh
venv\Scripts\activate
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Run

```sh
python main.py
```

---

## 🐧 Linux / Ubuntu / WSL

### Update System

```sh
sudo apt update && sudo apt upgrade -y
```

### Install Python & Git

```sh
sudo apt install python3 python3-pip python3-venv git -y
```

### Clone Repository

```sh
git clone https://github.com/Marvelusz/MarvelTools.git
```

### Enter Project Directory

```sh
cd MarvelTools
```

### Create Virtual Environment

```sh
python3 -m venv venv
```

### Activate Virtual Environment

```sh
source venv/bin/activate
```

### Install Dependencies

```sh
pip3 install -r requirements.txt
```

### Run

```sh
python3 main.py
```

---

## 📱 Termux (Android)

### Update Packages

```sh
pkg update && pkg upgrade -y
```

### Install Dependencies

```sh
pkg install python git clang -y
```

### Clone Repository

```sh
git clone https://github.com/Marvelusz/MarvelTools.git
```

### Enter Project Directory

```sh
cd MarvelTools
```

### Install Python Packages

```sh
pip install -r requirements.txt
```

### Run

```sh
python main.py
```