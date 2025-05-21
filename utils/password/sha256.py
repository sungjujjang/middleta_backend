from settings import setting
import hashlib

def encrypt(password):
    password = password.encode('utf-8')
    hashed_password = hashlib.sha256(password).hexdigest()
    return hashed_password

def decrypt(encrypted_password, password):
    check_password = encrypt(password)
    if encrypted_password == check_password:
        return True
    else:
        return False