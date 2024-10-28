import random
import string

def generate_password(length, include_special_chars=True):
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))
include_special = input("Include special characters? (y/n): ").lower() == 'y'
print("Generated password:", generate_password(length, include_special))
