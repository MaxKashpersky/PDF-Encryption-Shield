# PDF Encryption Shield 🔒

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

A professional Python application for securing PDF documents through encryption and decryption with password protection. Built with **PyPDF2** for reliable PDF manipulation.

---

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technical Details](#-technical-details)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## ✨ Features
- 🔐 PDF Encryption — Add strong password protection to PDF files  
- 🔓 PDF Decryption — Remove password protection from encrypted PDFs  
- 🛡️ Security Focused — Uses standard PDF encryption algorithms  
- 💻 User-Friendly CLI — Clean command-line interface with input validation  
- 🚀 Lightweight — Minimal dependencies  
- 📁 File Safety — Original files stay untouched  

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Quick Setup

Clone the repository:

```bash
git clone https://github.com/MaxKashpersky/PDF-Encryption-Shield.git
cd PDF-Encryption-Shield
```

Install dependencies:

    pip install PyPDF2

Or install from requirements:

    pip install -r requirements.txt

---

## 🚀 Usage

Run the application:

    python main.py

### Application Workflow

**Main Menu**

    ==================================================
              PDF ENCRYPTION/DECRYPTION TOOL
    ==================================================
    1. Encrypt PDF (Add password protection)
    2. Decrypt PDF (Remove password protection)
    3. Exit
    ==================================================

### 🔐 Encrypting a PDF File
1. Choose option 1  
2. Enter path to the PDF  
3. Set password (min 3 chars)  
4. Choose output filename  
5. Encrypted file is created  

### 🔓 Decrypting a PDF File
1. Choose option 2  
2. Enter path to encrypted PDF  
3. Enter password  
4. Choose output filename  
5. Decrypted file is created  

---

## 📘 Example Session

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

---


## 🔧 Technical Details
- Library: PyPDF2 3.0.0+  
- Encryption: RC4 or AES  
- PDF Compatibility: PDF 1.4–1.7  
- Validation: Checks for file existence, file extension, password  
- Error Handling: User-friendly messages  
- Output: Creates new files without touching originals  

---

## 📁 Project Structure

    PDF-Encryption-Shield/
    ├── main.py                 # Main application entry point
    ├── README.md              # Documentation
    ├── .gitignore             # Git ignore rules
    └── requirements.txt       # Dependencies

### Key Functions
- encrypt_pdf() — performs PDF encryption  
- decrypt_pdf() — decrypts password-protected PDFs  
- display_menu() — CLI menu  
- main() — application workflow  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a new branch:

        git checkout -b feature/YourFeature

3. Commit changes:

        git commit -m "Add YourFeature"

4. Push branch:

        git push origin feature/YourFeature

5. Open a Pull Request  

### Development Setup

        git clone https://github.com/MaxKashpersky/PDF-Encryption-Shield.git
        cd PDF-Encryption-Shield
        python -m venv .venv
        source .venv/bin/activate      # On Windows: .venv\Scripts\activate
        pip install -r requirements.txt

---

## 📄 License
This project is licensed under the MIT License.  
See the LICENSE file for details.

---

## 👨‍💻 Author
**Max Kashpersky**  
GitHub: @MaxKashpersky  
Email: 220718354+MaxKashpersky@users.noreply.github.com  

---

## 💬 Support
If you need help or found a bug:

- Check Issues
- Create a new Issue describing:
  - Problem
  - Steps to reproduce
  - Expected behavior
  - Actual behavior  

---

## ⚠️ Legal Disclaimer
This tool is intended only for legal and authorized use.  
Users must comply with all laws and ensure they own or have rights to the files.

---

⭐ If you find this project useful — please star it on GitHub!
