from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256
from stegano import lsb
import base64
from PIL import Image

# Prompt the user for a password, hash it using SHA-256, and return a 32-byte key.
def get_hashed_key(password):
    hashed_key = SHA256.new(password.encode()).digest()  # Generate a 32-byte hash
    return hashed_key

# Decryption
def decrypt_text(encrypted_text, key):
    encrypted_bytes = base64.b64decode(encrypted_text)  
    iv = encrypted_bytes[:16]  
    cipher = AES.new(key, AES.MODE_CBC, iv)  
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes[16:]), AES.block_size)  # Decrypt & unpad
    return decrypted_bytes.decode()  # Convert bytes to String

# Extract the hidden encrypted text from the image and decrypt it.
def reveal_text_from_image(stego_image_path, key):
    try:
        image = Image.open(stego_image_path).convert("RGB")
        encrypted_text = lsb.reveal(image)  # Extract encrypted text from image
    except IndexError:
        return None, "No hidden message found in the image!"
    
    if encrypted_text is None:
        return None, "No hidden message found in the image!"
    try:
        decrypted_message = decrypt_text(encrypted_text, key)  # Decrypt extracted text
        return decrypted_message, "Decrypted successfully!"
    except Exception as e:
        return None, "Decryption failed! Incorrect password or corrupted data."