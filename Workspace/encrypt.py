from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from stegano import lsb
import base64
from PIL import Image

# Prompt the user for a password, hash it using SHA-256, and return a 32-byte key.
def get_hashed_key(password):
    hashed_key = SHA256.new(password.encode()).digest()  
    return hashed_key

# Encrypt text using AES-CBC and return Base64-encoded ciphertext.
def encrypt_text(plain_text, key):
    iv = get_random_bytes(16)  # Generate a random 16-byte IV
    cipher = AES.new(key, AES.MODE_CBC, iv)  
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size)) 
    return base64.b64encode(iv + encrypted_bytes).decode() 

# Encrypt the text and hide it inside an image using LSB steganography.
def hide_text_in_image(secret_text, input_image, output_image, key):
    encrypted_text = encrypt_text(secret_text, key)
    image = Image.open(input_image).convert("RGB")
    stego_image = lsb.hide(image, encrypted_text)
    stego_image.save(output_image)
    return "Secret message encrypted and hidden in the image successfully!"