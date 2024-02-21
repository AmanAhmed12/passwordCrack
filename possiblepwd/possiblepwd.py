import itertools
import string

def generate_all_passwords(pwd_length):
    possible_chars = string.ascii_letters + string.digits
    for p in itertools.product(possible_chars, repeat=pwd_length):
        yield ''.join(p)

def display_all_passwords(pwd_length):
    print("Generating all possible password guesses...")
    for idx, guess in enumerate(generate_all_passwords(pwd_length), start=1):
        print(f"Password guess {idx}: {guess}")

def crack_password(pwd, possible_passwords):
    attempts = 0
    for guess in possible_passwords:
        attempts += 1
        if guess == pwd:
            print(f"The password was cracked in {attempts} attempts.")
            print(f"The password cracked was: {guess}")
            return
    
    print("Password not found in the generated list.")


password_length = int(input("Enter the password length: "))

possible_passwords= generate_all_passwords(password_length)

user_password = input("Enter the password to crack: ")
crack_password(user_password,possible_passwords)
with open('possible_passwords', 'w') as possible_file:
        for idx, guess in enumerate(generate_all_passwords(password_length), start=1):
            possible_file.write(f"Password guess {idx}: {guess}\n")