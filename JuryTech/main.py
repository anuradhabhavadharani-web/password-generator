import secrets

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

all_chars = letters + numbers + symbols

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += secrets.choice(all_chars)

print("Your generated password is:", password)
