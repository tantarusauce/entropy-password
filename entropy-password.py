# password_generator
# You are free to use this code anywhere.
#
# 2026 tantarusauce

version = "0.3"

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

def generate_password(length, char_list):
    return ''.join(secrets.choice(char_list) for _ in range(length))

def print_password(length, char_list, copy):
    password = generate_password(length, char_list)
    print("\nGenerated password:\n")
    print(password)
    print("\nLength:", length)
    print("Character set size:", len(char_list))
    entropy = length * math.log2(len(char_list))
    print("Entropy:", round(entropy, 2), "bits")
    if copy:
        if pyperclip:
            pyperclip.copy(password)
            print("Copied to clipboard.")
        else:
            print("Clipboard feature requires the 'pyperclip' package.")
    print()

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


# CLI Mode
if args.length is not None:

    available_chars = ""

    if args.uppercase:
        available_chars += string.ascii_uppercase

    if args.lowercase:
        available_chars += string.ascii_lowercase

    if args.numbers:
        available_chars += string.digits

    if args.symbols == "auto":
        args.symbols = string.punctuation

    available_chars += args.symbols

    char_list = tuple(set(available_chars))

    if args.length <= 0:
        print("Error: Length must be a positive number.")
        sys.exit()
    
    if not char_list:
        print("Error: No characters available.")
        sys.exit()

    print_password(args.length, char_list, args.copy)

    sys.exit()


# Interactive Mode
while True:
    available_chars = ""

    length = ask_password_length()

    if ask_yes_no("Allow uppercase letters?"):
        available_chars += string.ascii_uppercase

    if ask_yes_no("Allow lowercase letters?"):
        available_chars += string.ascii_lowercase

    if ask_yes_no("Allow numbers?"):
        available_chars += string.digits

    print("Enter additional characters (type 'auto' for common symbols)\n> ")
    additional_chars = input()
    
    if additional_chars == "auto":
        available_chars += string.punctuation
    else:
        available_chars += additional_chars

    char_list = tuple(set(available_chars))

    if not char_list:
        print("No characters available. Please start over.\n")
        continue

    copy = ask_yes_no("Copy to clipboard?")
    break

print_password(length, char_list, copy)