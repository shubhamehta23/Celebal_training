
password = input("Enter the password: ")

has_digit = False
has_uppercase = False

for char in password:
    if char.isdigit():
        has_digit = True

    if char.isupper():
        has_uppercase = True

if len(password) >= 8 and has_digit and has_uppercase:
    print("STRONG")
else:
    print("WEAK")
