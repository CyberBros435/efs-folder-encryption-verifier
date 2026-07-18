````markdown
# 🔐 EFS Folder Encryption Verifier

A lightweight Python-based command-line utility for verifying the **Encrypting File System (EFS)** status of folders on Windows using the native **cipher.exe** command.

This project helps users, system administrators, students, and cybersecurity learners quickly determine whether a folder is protected with Microsoft's Encrypting File System (EFS).

---

## 📖 Overview

The **EFS Folder Encryption Verifier** is designed to simplify checking whether a folder is encrypted using the Windows Encrypting File System (EFS).

Instead of manually opening Command Prompt and typing Windows commands, this tool automates the process and displays the encryption status in a clean and organized format.

The utility leverages the built-in Windows **cipher** command through Python's `subprocess` module, making it lightweight with no third-party dependencies.

---

# ✨ Features

- ✅ Verify EFS encryption status of any folder
- ✅ Uses the native Windows `cipher` utility
- ✅ Command-line interface (CLI)
- ✅ User-friendly output
- ✅ Folder existence validation
- ✅ Exception handling
- ✅ Displays Windows EFS information
- ✅ Lightweight and fast
- ✅ No external Python libraries required
- ✅ Beginner-friendly source code
- ✅ Open-source and customizable

---

# 📂 Project Structure

```
efs-folder-encryption-verifier/
│
├── efs_verifier.py
├── README.md
├── Project_Report.pdf
└── LICENSE (Optional)
```

---

# 🛠 Requirements

## Operating System

- Windows 10
- Windows 11
- Windows Server

---

## File System

The target folder must reside on an **NTFS** partition because EFS is only supported on NTFS.

---

## Python Version

Python 3.8+

Check your version:

```bash
python --version
```

---

## Required Module

Only Python standard libraries are used.

- argparse
- subprocess
- os
- sys

No installation is required.

---

# 📥 Installation

## Clone Repository

```bash
git clone https://github.com/CyberBros435/efs-folder-encryption-verifier.git
```

Move into the project folder

```bash
cd efs-folder-encryption-verifier
```

---

# 🚀 Usage

Basic syntax

```bash
python efs_verifier.py "Folder_Path"
```

---

## Example

```bash
python efs_verifier.py "D:\SecretFolder"
```

Another example

```bash
python efs_verifier.py "C:\Users\John\Documents"
```

---

# 📸 Example Output

```
========== EFS VERIFICATION ==========
Target Folder : D:\SecretFolder
--------------------------------------

 Listing D:\SecretFolder

 New files added to this directory will not be encrypted.

 E SecretFolder

======================================
```

---

# 🔍 How It Works

The application performs the following steps:

1. Accepts a folder path from the command line.
2. Checks whether the folder exists.
3. Executes Windows `cipher /c`.
4. Captures the command output.
5. Displays the encryption information.
6. Handles possible errors gracefully.

---

# 💻 Technologies Used

- Python
- Windows Command Line
- subprocess
- argparse
- Windows Encrypting File System (EFS)

---

# 🪟 Windows Command Used

The tool internally executes:

```bash
cipher /c <Folder_Path>
```

Example

```bash
cipher /c D:\SecretFolder
```

This command checks the encryption status of the specified folder.

---

# ⚠ Error Handling

The application handles several common issues.

## Folder Not Found

```
[ERROR] Folder does not exist.
```

---

## Cipher Command Not Available

```
[ERROR] 'cipher' command was not found.
```

---

## Invalid Path

Displays a clear error message and exits safely.

---

# 📌 Supported Platforms

| Platform | Supported |
|----------|-----------|
| Windows 10 | ✅ |
| Windows 11 | ✅ |
| Windows Server | ✅ |
| Linux | ❌ |
| macOS | ❌ |

---

# 📚 Learning Objectives

This project demonstrates practical knowledge of:

- Python Programming
- subprocess Module
- Command-Line Applications
- Windows Security
- Windows Encrypting File System (EFS)
- File System Security
- Error Handling
- Input Validation
- Secure Administrative Utilities

---

# 🎯 Use Cases

This tool can be used by:

- Cybersecurity Students
- SOC Analysts
- Blue Team Members
- System Administrators
- IT Support Engineers
- Windows Administrators
- Digital Forensics Learners

---

# 🔒 About Encrypting File System (EFS)

Encrypting File System (EFS) is a Windows security feature that enables transparent encryption of files and folders stored on NTFS drives.

Unlike BitLocker, which encrypts an entire disk, EFS encrypts individual files and folders for user-level protection.

Learn more:
https://learn.microsoft.com/windows/security/

---

# ⚠ Limitations

- Windows only
- Requires NTFS file system
- Requires Windows EFS support
- Does not encrypt folders
- Does not decrypt folders
- Only verifies encryption status

---

# 🔮 Future Improvements

Potential future enhancements include:

- Colored terminal output
- JSON export
- CSV export
- Recursive folder scanning
- GUI version
- Logging support
- Batch folder verification
- Automatic EFS status detection
- Report generation
- PowerShell integration

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 🐞 Reporting Issues

If you encounter a bug or have a feature request, please create an Issue on GitHub describing:

- Problem
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)

---

# 📄 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project with proper attribution.

---

# 👨‍💻 Author

**Mudasir Zia**

Cybersecurity Student

GitHub:
https://github.com/CyberBros435

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🐛 Report issues

💡 Suggest improvements

---

# 📌 Disclaimer

This project is intended for educational and administrative purposes only.

It does not modify, encrypt, decrypt, or alter any files. It simply verifies the encryption status of folders using the native Windows `cipher` utility.

---

## 📜 Version

**Current Version:** 1.0.0

---

## 📧 Contact

For suggestions, improvements, or collaboration, feel free to connect through GitHub.

---

**If you found this project helpful, don't forget to ⭐ star the repository!**
````
