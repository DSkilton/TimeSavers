import hashlib
import random
import string

# crack_me = 'f76b61b962db075bb76ad6f3fab10f7bd546f92f1b89f18c513d4122575c18ac'
crack_me = 'd70980fa9087a50848b6a445ea705e1d7a9c7afcacd8c43f7577dfe52fef5eb7'

def password_list():
    count = 0
    with open("plainTextPass.txt", "r") as passwords:
        for password in passwords:
            cleaned = password.strip()            
            count += 1
            if crack_me == hash_function(cleaned):
                print("Password: " + password)
                print(count)
                break
            

def hash_function(plaintext):
    encoded_plaintext = plaintext.encode()
    hashed = hashlib.sha256(encoded_plaintext).hexdigest()
    return hashed


password_list()
