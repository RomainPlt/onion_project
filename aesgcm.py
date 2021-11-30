from Cryptodome.Cipher import AES
import hashlib
import sys
import binascii

from sender import encrypt_message


def encrypt(plaintext,key, mode):
  encobj = AES.new(key, AES.MODE_GCM)
  ciphertext,authTag=encobj.encrypt_and_digest(plaintext)
  return(ciphertext,authTag,encobj.nonce)

def decrypt(ciphertext,key, mode):
  (ciphertext,  authTag, nonce) = ciphertext
  encobj = AES.new(key,  mode, nonce)
  return(encobj.decrypt_and_verify(ciphertext, authTag))


def main(plaintext, password, is_encrypting):
  key = hashlib.sha256(password.encode()).digest()
  if is_encrypting:
    ciphertext = encrypt(plaintext.encode(),key,AES.MODE_GCM)
    return ciphertext
  else:
    res= decrypt(plaintext,key,AES.MODE_GCM)
    return res


