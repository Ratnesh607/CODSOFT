import random
import string

def generate_password(num_letters, num_digits, num_symbols):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password_letters = [random.choice(letters) for _ in range(num_letters)]
    password_digits = [random.choice(digits) for _ in range(num_digits)]
    password_symbols = [random.choice(symbols) for _ in range(num_symbols)]

    password_list = password_letters + password_digits + password_symbols

    random.shuffle(password_list)

    password = ''.join(password_list)
    return password

print (" Welcome to the Password Generator")

try:
    num_letters = int(input("Enter the number of letters: "))
    num_digits = int(input("Enter the number of digits: "))
    num_symbols = int(input("Enter the number of symbols: "))

    total_length = num_letters + num_digits + num_symbols

    if total_length < 4:
        print("\n Password should have at least 4 characters for better security. ")

    else:
        password = generate_password(num_letters, num_digits, num_symbols)
        print(f"\n Your generated password is: {password}")
        print(f"Password length: {len(password)} character")
        print(f"Contains: {num_letters} letters, {num_digits} digits, {num_symbols} symbols")

except ValueError:
    print("\n Plese enter a valid number!")

