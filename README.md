# 🔐 EFS Folder Encryption Verifier

A simple Python tool that checks if a Windows folder is encrypted using EFS (Encrypting File System) — by running Windows' built-in `cipher /c` command and showing the result in a clean, easy-to-read format.

![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

## 📌 Overview

Windows shows a padlock icon on encrypted folders, but that icon can be unreliable — for example, it can be hidden when the folder is inside OneDrive. This tool skips the icon and checks the real encryption status directly from Windows using `cipher /c`.

Works on any folder path on any Windows PC — just give it your own folder path.

## ⚠️ Requirements

| Requirement | Notes |
|---|---|
| OS | Windows only (EFS is a Windows/NTFS feature — will not work on macOS/Linux) |
| Windows Edition | Pro / Enterprise / Education (EFS is not available on Windows Home) |
| Python | 3.8 or higher |
| Git | Needed to clone the repo |

## 🚀 Installation & Setup (Step by Step)

### 1. Install Python
Download: https://python.org/downloads
⚠️ During install, check the box "Add Python to PATH."

```bash
python --version
```

### 2. Install Git
Download: https://git-scm.com/download/win

```bash
git --version
```

### 3. Clone this repository
```bash
git clone https://github.com/CyberBros435/efs-folder-encryption-verifier.git
```

### 4. Move into the project folder
```bash
cd efs-folder-encryption-verifier
```

### 5. Run the script
```bash
python efs_verifier.py
```
This checks the current folder by default. To check a different folder, open `efs_verifier.py` and change the `target` path at the top of the file to your own folder's full path.

## 🖥️ Usage Example

Sample output when a folder is encrypted:
