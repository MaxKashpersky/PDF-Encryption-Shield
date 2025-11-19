# PDF Encryption Shield 🔒

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

A professional Python application for securing PDF documents through encryption and decryption with password protection. Built with PyPDF2 for reliable PDF manipulation.

## 📋 Table of Contents

- [Features](#features-)
- [Installation](#installation-)
- [Usage](#usage-)
- [Screenshots](#screenshots-)
- [Technical Details](#technical-details-)
- [Project Structure](#project-structure-)
- [Contributing](#contributing-)
- [License](#license-)
- [Support](#support-)

## Features ✨

- **🔐 PDF Encryption** - Add strong password protection to PDF files
- **🔓 PDF Decryption** - Remove password protection from encrypted PDFs
- **🛡️ Security Focused** - Uses standard PDF encryption algorithms
- **💻 User-Friendly CLI** - Clean command-line interface with comprehensive input validation
- **🚀 Lightweight** - Minimal dependencies, fast performance
- **📁 File Safety** - Preserves original files, creates new encrypted/decrypted copies

## Installation 📦

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Setup

1. **Clone the repository:**
```bash
git clone https://github.com/MaxKashpersky/PDF-Encryption-Shield.git
cd PDF-Encryption-Shield
Install dependencies:

bash
pip install PyPDF2
Or use the requirements file:

bash
pip install -r requirements.txt
Usage 🚀
Run the application:

bash
python main.py
Application Workflow
Main Menu:
text
==================================================
          PDF ENCRYPTION/DECRYPTION TOOL
==================================================
1. Encrypt PDF (Add password protection)
2. Decrypt PDF (Remove password protection)
3. Exit
==================================================
Encrypting a PDF File:
Choose option 1 from the menu

Enter the path to your PDF file

Set a strong password (minimum 3 characters)

Specify output filename

The encrypted file will be created with password protection

Decrypting a PDF File:
Choose option 2 from the menu

Enter the path to the encrypted PDF

Provide the correct password

Specify output filename for the decrypted version

The decrypted file will be created without password protection

Example Session
bash
$ python main.py

Welcome to the PDF Security Tool!

==================================================
          PDF ENCRYPTION/DECRYPTION TOOL
==================================================
1. Encrypt PDF (Add password protection)
2. Decrypt PDF (Remove password protection)
3. Exit
==================================================

Please choose an option (1-3): 1

=== PDF Encryption ===
Enter the path to the PDF file to encrypt: confidential.pdf
Enter encryption password: ********
Enter name for the encrypted file (without extension): secured_document

✅ Success! Encrypted file 'secured_document.pdf' created with password protection.
Screenshots 📸
(You can add screenshots of your application interface here)

Technical Details 🔧
Library: PyPDF2 3.0.0+

Encryption: Standard PDF encryption (RC4 or AES)

Compatibility: Works with PDF 1.4-1.7 specifications

Input Validation: Comprehensive file existence, format, and password checks

Error Handling: Robust exception handling with user-friendly messages

Output: Creates new files while preserving originals

Project Structure 📁
text
PDF-Encryption-Shield/
├── main.py                 # Main application entry point
├── README.md              # Project documentation
├── .gitignore            # Git ignore rules
└── requirements.txt      # Python dependencies
Key Functions:
encrypt_pdf() - Handles PDF encryption with password

decrypt_pdf() - Manages PDF decryption process

display_menu() - Shows user interface menu

main() - Application controller and workflow manager

Contributing 🤝
We welcome contributions! Please follow these steps:

Fork the repository

Create a feature branch: git checkout -b feature/YourFeature

Commit your changes: git commit -m 'Add YourFeature'

Push to the branch: git push origin feature/YourFeature

Open a Pull Request

Development Setup:
bash
git clone https://github.com/MaxKashpersky/PDF-Encryption-Shield.git
cd PDF-Encryption-Shield
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

Author 👨‍💻
Max Kashpersky

GitHub: @MaxKashpersky

Email: 220718354+MaxKashpersky@users.noreply.github.com

Created as part of my software development and testing portfolio.

Support 💬
If you need help or found a bug:

Check existing Issues

Create a New Issue with:

Detailed description

Steps to reproduce

Expected vs actual behavior

⚠️ Legal Disclaimer
This tool is designed for legitimate purposes such as:

Protecting personal documents

Securing sensitive business files

Educational and learning purposes

Users are responsible for ensuring they have proper authorization to encrypt/decrypt any files and must comply with all applicable laws and copyright regulations.

⭐ If you find this project useful, please give it a star on GitHub!