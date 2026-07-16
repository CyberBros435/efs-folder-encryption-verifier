# 🔐 EFS Folder Encryption Verifier

A lightweight Python CLI tool that verifies whether a Windows folder is protected using **EFS (Encrypting File System)** — by wrapping and parsing the native Windows `cipher /c` command into a clean, readable report.

![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Overview

Windows shows a padlock icon on encrypted folders — but that icon can be **unreliable** (e.g., hidden by OneDrive sync). This tool skips the icon entirely and checks the **real, authoritative encryption status** directly from Windows using `cipher /c`, then presents it in a clean, script-friendly format.

Built as a hands-on cybersecurity mini-project demonstrating:
- Windows EFS (data-at-rest encryption)
- Python `subprocess` — running & parsing external system commands
- Practical security verification (not trusting UI indicators blindly)

---

## ⚠️ Requirements

| Requirement | Notes |
|---|---|
| **OS** | Windows only (EFS is a Windows/NTFS-specific feature — will NOT run on macOS/Linux) |
| **Windows Edition** | Pro / Enterprise / Education (EFS is **not available** on Windows Home) |
| **Python** | 3.8 or higher |
| **Git** | Required to clone the repo |

---

## 🚀 Installation & Setup (Step by Step)

### 1. Install Python (skip if already installed)
Download from: https://python.org/downloads

⚠️ **During install, check the box "Add Python to PATH"** — required or Step 2 will fail.

Verify installation:
```bash
python --version
```
Expected output: `Python 3.x.x`

---

### 2. Install Git (skip if already installed)
Download from: https://git-scm.com/download/win

Verify installation:
```bash
git --version
```

---

### 3. Clone this repository
```bash
git clone https://github.com/CyberBros435/efs-folder-encryption-verifier.git
```

### 4. Move into the project folder
```bash
cd efs-folder-encryption-verifier
```

### 5. Run the tool
```bash
python efs_verifier.py "D:\path\to\your\folder"
```

If no path is given, the script checks the current directory by default.

---

## 🖥️ Usage Example

```bash
python efs_verifier.py "D:\SOC_Projects\Assignment_Folder"
```

**Sample Output:**
