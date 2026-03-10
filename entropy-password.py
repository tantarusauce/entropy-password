# password_generator
# You are free to use this code anywhere.
#
# 2026 tantarusauce

version = "0.4.0"

import secrets
import string
import argparse
import sys
import math

try:
    import pyperclip
except ImportError:
    pyperclip = None

def ask_yes_no(message):
    while True:
        print(message + " (y/n)\n> ", end="")
        answer = input().lower()

        if answer in ("y", "n"):
            return answer == "y"

        print("Invalid input. Please enter y or n.")


def ask_password_length():
    while True:
        try:
            print("Enter the password length (numbers only).\n> ", end="")
            length = int(input())

            if length <= 0:
                print("Error: Please enter a positive number.")
                continue

            return length

        except ValueError:
            print("Error: Please enter numbers only.")

def generate_password(length, char_list, sets):
    if not char_list:
        raise ValueError("Character list cannot be empty")

    password = []

    # Pick one character from each category
    for s in sets:
        if s:
            idx = secrets.randbelow(len(s))
            password.append(s.pop(idx))

    # Pick the rest from the available characters
    available_chars = char_list.copy()
    while len(password) < length:
        if not available_chars:
            available_chars = char_list.copy()
        idx = secrets.randbelow(len(available_chars))
        password.append(available_chars.pop(idx))

    # Mix/shuffle the result
    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]

    return password

def print_password(length, char_list, copy, sets):
    password = generate_password(length, char_list, sets)
    print("\nGenerated password:\n")
    print(password)
    print("\nLength:", length)
    print("Character set size:", len(char_list))
    print("Entropy:", round(entropy_without_repetition(length, len(char_list)), 2), "bits")
    if copy:
        if pyperclip:
            pyperclip.copy(password)
            print("Copied to clipboard.")
        else:
            print("Clipboard feature requires the 'pyperclip' package.")
    print()

def entropy_without_repetition(length, char_set_size):
    if length > char_set_size:
        # First cycle: no repetition, then reset if needed
        # 1st cycle
        k1 = char_set_size  # character count
        entropy1 = sum(math.log2(k1 - i) for i in range(char_set_size))
        # From 2nd cycle onward, use regular random selection
        remaining = length - char_set_size
        entropy2 = remaining * math.log2(char_set_size)
        return entropy1 + entropy2
    else:
        # If all characters fit without repetition
        return sum(math.log2(char_set_size - i) for i in range(length))

parser = argparse.ArgumentParser(
    description="A simple CLI password generator using Python's secrets module"
)

parser.add_argument("--length", type=int, help="Password length")
parser.add_argument("--uppercase", action="store_true", help="Allow uppercase letters")
parser.add_argument("--lowercase", action="store_true", help="Allow lowercase letters")
parser.add_argument("--numbers", action="store_true", help="Allow numbers")
parser.add_argument("--symbols", type=str, default="", help="Additional characters (use 'auto' for common symbols)")
parser.add_argument("--version", action="version", version="entropy-password-generator " + version)
parser.add_argument("--copy", action="store_true", help="Copy the generated password to the clipboard")

args = parser.parse_args()
sets = list()

# CLI Mode
if args.length is not None:

    available_chars = ""

    if args.uppercase:
        available_chars += string.ascii_uppercase
        sets.append(list(string.ascii_uppercase))

    if args.lowercase:
        available_chars += string.ascii_lowercase
        sets.append(list(string.ascii_lowercase))

    if args.numbers:
        available_chars += string.digits
        sets.append(list(string.digits))

    if args.symbols == "auto":
        available_chars += string.punctuation
        sets.append(list(string.punctuation))
    else:
        available_chars += args.symbols
        sets.append(list(args.symbols))

    char_list = list(set(available_chars)) # Delete same characters

    if args.length <= 0:
        print("Error: Length must be a positive number.")
        sys.exit()
    
    if not char_list:
        print("Error: No characters available.")
        sys.exit()

    print_password(args.length, char_list, args.copy, sets)

    sys.exit()


# Interactive Mode
while True:
    available_chars = ""

    length = ask_password_length()

    if ask_yes_no("Allow uppercase letters?"):
        available_chars += string.ascii_uppercase
        sets.append(list(string.ascii_uppercase))

    if ask_yes_no("Allow lowercase letters?"):
        available_chars += string.ascii_lowercase
        sets.append(list(string.ascii_lowercase))

    if ask_yes_no("Allow numbers?"):
        available_chars += string.digits
        sets.append(list(string.digits))

    print("Enter additional characters (type 'auto' for common symbols)\n> ", end="")
    additional_chars = input()
    
    if additional_chars == "auto":
        available_chars += string.punctuation
        sets.append(list(string.punctuation))
    else:
        available_chars += additional_chars
        sets.append(list(additional_chars))

    char_list = list(set(available_chars)) # Delete same characters

    if not char_list:
        print("No characters available. Please start over.\n")
        continue

    copy = ask_yes_no("Copy to clipboard?")
    break

print_password(length, char_list, copy, sets)