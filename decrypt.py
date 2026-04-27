from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256
from stegano import lsb
import base64

# Prompt the user for a password, hash it using SHA-256, and return a 32-byte key.
def get_hashed_key():
    password = input("Enter the decryption password: ").encode()  # Convert to bytes
    hashed_key = SHA256.new(password).digest()  # Generate a 32-byte hash
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
    encrypted_text = lsb.reveal(stego_image_path)  # Extract encrypted text from image
    if encrypted_text is None:
        print("\nNo hidden message found in the image!")
        return None
    try:
        decrypted_message = decrypt_text(encrypted_text, key)  # Decrypt extracted text
        print("\nDecrypted Message:", decrypted_message)
        return decrypted_message
    except Exception as e:
        print("\nDecryption failed! Incorrect password or corrupted data.")
        return None
'''
# For Terminal Udage
# User input
key = get_hashed_key()  # Generate AES key from hashed password
stego_image_path = "stego.png"  # Replace with your image path

# Extract & decrypt the hidden message
reveal_text_from_image(stego_image_path, key)'''
