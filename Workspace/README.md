# Image Steganography Web App

A web application for hiding and revealing secret messages in images using AES encryption and LSB steganography.

## Features

- Encrypt a secret message into an image
- Decrypt a message from an encrypted image
- Secure AES encryption with password protection

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open http://localhost:5000 in your browser.

## Deployment to Vercel

1. Push this code to a GitHub repository.

2. Connect your GitHub repo to Vercel.

3. Vercel will automatically detect the `vercel.json` and deploy the Flask app.

## Usage

- **Encrypt**: Upload a cover image, enter your secret message and password, then download the encrypted image.
- **Decrypt**: Upload the encrypted image and enter the password to reveal the hidden message.