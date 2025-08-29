import random
import string

length = input("Enter desired password length (minimum 6): ")

if not length.isdigit() or int(length) < 6:
    print("Invalid input. Using default length of 8.")
    length = 8
else:
    length = int(length)

characters = string.ascii_letters + string.digits + string.punctuation

password = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
]

password += random.choices(characters, k=length - 4)

random.shuffle(password)

final_password = ''.join(password)

print("\nYour generated password is:")
print(final_password)
