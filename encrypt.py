from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from stegano import lsb
import base64

# Prompt the user for a password, hash it using SHA-256, and return a 32-byte key.
def get_hashed_key():
    password = input("Enter an encryption password: ").encode()  
    hashed_key = SHA256.new(password).digest()  
    # print(hashed_key)
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
    stego_image = lsb.hide(input_image, encrypted_text)
    stego_image.save(output_image)
    print("\nSecret message encrypted and hidden in the image successfully!")
'''
# For terminal usage
# User input
key = get_hashed_key()  # Generate AES key from hashed password
message = input("\nEnter the secret message: ")  # Message to hide
input_image_path = "input.png"  
output_image_path = "stego.png"  

# Encrypt & hide the message
hide_text_in_image(message, input_image_path, output_image_path, key)
'''
