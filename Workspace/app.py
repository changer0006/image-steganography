from flask import Flask, request, render_template, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
import encrypt
import decrypt
from PIL import Image
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = '/tmp'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    print("Encrypt route called")
    if 'cover_image' not in request.files:
        flash('No cover image uploaded')
        return redirect(url_for('index'))
    
    cover_file = request.files['cover_image']
    secret_message = request.form['message']
    password = request.form['password']
    
    if cover_file.filename == '' or not secret_message or not password:
        print("Fields missing")
        flash('All fields are required')
        return redirect(url_for('index'))
    
    filename = secure_filename(cover_file.filename)
    cover_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    cover_file.save(cover_path)
    print(f"Cover saved to {cover_path}")
    
    key = encrypt.get_hashed_key(password)
    base_name = os.path.splitext(filename)[0]
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encrypted_' + base_name + '.png')
    encrypt.hide_text_in_image(secret_message, cover_path, output_path, key)
    print(f"Encrypted to {output_path}")
    
    return send_file(output_path, as_attachment=True, download_name='encrypted_image.png')

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    print("Decrypt route called")
    if 'encrypted_image' not in request.files:
        print("No encrypted_image in files")
        flash('No encrypted image uploaded')
        return redirect(url_for('index'))
    
    encrypted_file = request.files['encrypted_image']
    password = request.form['password']
    
    if encrypted_file.filename == '' or not password:
        print("Filename empty or no password")
        flash('All fields are required')
        return redirect(url_for('index'))
    
    filename = secure_filename(encrypted_file.filename)
    encrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    encrypted_file.save(encrypted_path)
    print(f"File saved to {encrypted_path}")
    
    key = decrypt.get_hashed_key(password)
    message, status = decrypt.reveal_text_from_image(encrypted_path, key)
    print(f"Reveal result: message={message}, status={status}")
    
    if message:
        flash(f'Decrypted Message: {message}')
    else:
        flash(status)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)