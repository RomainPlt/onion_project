from Crypto.Cipher import AES
from simple_aes_cipher import AESCipher, generate_secret_key


def encrypt(message, password):
    secret_key = generate_secret_key(password)
    cipher = AESCipher(secret_key)
    encrypted_text = cipher.encrypt(message)
    return encrypted_text


def decrypt(message, password):
    secret_key = generate_secret_key(password)
    cipher = AESCipher(secret_key)
    decrypted_text = cipher.decrypt(message)
    return decrypted_text
