# 🔐 Cryptosteg: Secure Image-Based Data Hiding

A cybersecurity project that combines **AES encryption** and **Least Significant Bit (LSB) steganography** to securely hide confidential information inside digital images.

## 📌 Overview

Cryptosteg provides an additional layer of security by encrypting secret data before embedding it into an image.

The project combines two techniques:
- **AES Encryption:** Encrypts confidential data to protect its contents.
- **LSB Steganography:** Hides encrypted data within the pixel values of an image.

The resulting image can be shared without directly exposing the hidden information.

## ✨ Features

- 🔒 AES-based data encryption
- 🖼️ LSB-based image steganography
- 🔑 Password-based protection (if implemented)
- 📤 Embed secret data into images
- 📥 Extract hidden data from images
- 🛡️ Two layers of security through encryption and steganography

## ⚙️ How It Works

1. **Input:** Provide the secret message or file.
2. **Encryption:** Encrypt the data using AES.
3. **Embedding:** Hide the encrypted data inside an image using LSB steganography.
4. **Image Output:** Generate an image containing the hidden information.
5. **Extraction:** Extract the encrypted data from the image.
6. **Decryption:** Decrypt the extracted data to recover the original information.

## 🛠️ Technologies Used

- Python
- AES Encryption
- Least Significant Bit (LSB) Steganography
- Image Processing
- Git & GitHub

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
