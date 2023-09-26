import hashlib

def encodePassword(password:str):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode())
    return sha256_hash.hexdigest()