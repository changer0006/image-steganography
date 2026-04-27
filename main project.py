# app.py
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import encrypt
import decrypt
from Crypto.Hash import SHA256

# --------------------- Root Window ---------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")  # Accent color
root = ctk.CTk()
root.title("Image Steganography")
root.geometry("600x500")

# --------------------- Functions ---------------------
def load_cover_image():
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    cover_image_entry.delete(0, ctk.END)
    cover_image_entry.insert(0, filename)
    display_image(filename, cover_image_label)

def load_encrypted_image():
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    encrypted_image_entry.delete(0, ctk.END)
    encrypted_image_entry.insert(0, filename)
    display_image(filename, encrypted_image_label)

def display_image(image_path, label):
    try:
        image = Image.open(image_path)
        image.thumbnail((150, 150))
        photo = ImageTk.PhotoImage(image)
        label.configure(image=photo)
        label.image = photo
    except Exception:
        messagebox.showerror("Error", "Cannot open image!")

def encrypt_message():
    secret_message = secret_message_entry.get()
    password = password_entry.get()
    cover_image = cover_image_entry.get()
    output_image = "encrypted_image.png"
    if secret_message and password and cover_image:
        key = SHA256.new(password.encode()).digest()
        encrypt.hide_text_in_image(secret_message, cover_image, output_image, key)
        messagebox.showinfo("Success", "Message encrypted and hidden successfully!")
    else:
        messagebox.showerror("Error", "All fields are required for encryption!")

def decrypt_message():
    password = decrypt_password_entry.get()
    encrypted_image = encrypted_image_entry.get()
    if password and encrypted_image:
        key = SHA256.new(password.encode()).digest()
        decrypted_text = decrypt.reveal_text_from_image(encrypted_image, key)
        decrypted_message_text.delete("1.0", ctk.END)
        decrypted_message_text.insert(ctk.END, decrypted_text if decrypted_text else "Decryption failed!")
    else:
        messagebox.showerror("Error", "All fields are required for decryption!")

# --------------------- Notebook Setup ---------------------
notebook = ctk.CTkTabview(root)
notebook.pack(pady=10, expand=True, fill="both")

# --------------------- Start Tab ---------------------
notebook.add("Start")
start_tab = notebook.tab("Start")
ctk.CTkLabel(start_tab, text="Choose an option:", font=("Helvetica", 16)).pack(pady=10)
ctk.CTkButton(start_tab, text="Encrypt", width=200, command=lambda: notebook.set("Encryption")).pack(pady=5)
ctk.CTkButton(start_tab, text="Decrypt", width=200, command=lambda: notebook.set("Decryption")).pack(pady=5)

# --------------------- Encryption Tab ---------------------
notebook.add("Encryption")
encryption_tab = notebook.tab("Encryption")

ctk.CTkLabel(encryption_tab, text="Load Image (For Encryption)").pack(pady=5)
cover_image_entry = ctk.CTkEntry(encryption_tab, width=400)
cover_image_entry.pack(pady=2)
ctk.CTkButton(encryption_tab, text="Select Image", command=load_cover_image).pack(pady=5)
cover_image_label = ctk.CTkLabel(encryption_tab, text="")
cover_image_label.pack(pady=5)

ctk.CTkLabel(encryption_tab, text="Secret Message:").pack(pady=2)
secret_message_entry = ctk.CTkEntry(encryption_tab, width=400)
secret_message_entry.pack(pady=2)

ctk.CTkLabel(encryption_tab, text="Passcode:").pack(pady=2)
password_entry = ctk.CTkEntry(encryption_tab, width=400, show="*")
password_entry.pack(pady=2)

ctk.CTkButton(encryption_tab, text="Encrypt", width=200, command=encrypt_message).pack(pady=10)

# --------------------- Decryption Tab ---------------------
notebook.add("Decryption")
decryption_tab = notebook.tab("Decryption")

ctk.CTkLabel(decryption_tab, text="Load Encrypted Image (For Decryption)").pack(pady=5)
encrypted_image_entry = ctk.CTkEntry(decryption_tab, width=400)
encrypted_image_entry.pack(pady=2)
ctk.CTkButton(decryption_tab, text="Select Image", command=load_encrypted_image).pack(pady=5)
encrypted_image_label = ctk.CTkLabel(decryption_tab, text="")
encrypted_image_label.pack(pady=5)

ctk.CTkLabel(decryption_tab, text="Passcode:").pack(pady=2)
decrypt_password_entry = ctk.CTkEntry(decryption_tab, width=400, show="*")
decrypt_password_entry.pack(pady=2)

ctk.CTkButton(decryption_tab, text="Decrypt", width=200, command=decrypt_message).pack(pady=10)

ctk.CTkLabel(decryption_tab, text="Decrypted Message:").pack(pady=2)
decrypted_message_text = ctk.CTkTextbox(decryption_tab, width=400, height=100)
decrypted_message_text.pack(pady=5)

# --------------------- Run App ---------------------
root.mainloop()
