import hashlib

def encodePassword(password:str):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(password.encode())
    password = hash_algorithm.hexdigest()
    print(password)
    return password