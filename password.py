import random
import string

# Gera uma senha forte com uma combinação de letras maiúsculas, minúsculas, números e símbolos
def generate_strong_password(length=16):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
