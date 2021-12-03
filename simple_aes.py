from Crypto.Cipher import AES
from simple_aes_cipher import AESCipher, generate_secret_key

"""pass_phrase = "hogefuga"
secret_key = generate_secret_key(pass_phrase)
print(secret_key)
# generate cipher
cipher = AESCipher(secret_key)
print(cipher)

raw_text = "{toto va a//} la plage http://localhost.com mdr va te faire foutre fdp"
encrypt_text = cipher.encrypt(raw_text)
print(encrypt_text)
assert raw_text != encrypt_text

decrypt_text = cipher.decrypt(encrypt_text)
print(decrypt_text)
assert encrypt_text != decrypt_text
assert decrypt_text == raw_text
"""

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