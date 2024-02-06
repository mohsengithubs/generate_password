import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    characters = string.ascii_letters
    if numbers:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    password = ""
    while len(password) < min_length:
        password += random.choice(characters)

    return password

password = generate_password(10, numbers=True, special_characters=True)
print(password)