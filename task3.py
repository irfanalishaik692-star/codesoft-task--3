import random
import string

# Prompt user for password length
length = int(input("Enter the desired password length: "))

# Define characters to use in password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Display the password
print("Generated Password:", password)