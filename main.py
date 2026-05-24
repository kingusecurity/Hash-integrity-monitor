import hashlib
from colorama import init, Fore
from datetime import datetime
import os

# Initialize colorama
init()

# Logging function
def write_log(message):

    with open("hash_log.txt", "a") as log_file:

        timestamp = datetime.now()

        log_file.write(
            f"[{timestamp}] {message}\n"
        )

# Generate MD5 hash
def generate_md5(text):

    return hashlib.md5(
        text.encode()
    ).hexdigest()

# Generate SHA256 hash
def generate_sha256(text):

    return hashlib.sha256(
        text.encode()
    ).hexdigest()

# Generate file hash
def hash_file(filepath):

    sha256 = hashlib.sha256()

    try:

        with open(filepath, "rb") as file:

            while True:

                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except:

        return None

# File integrity checker
def check_integrity(filepath, original_hash):

    current_hash = hash_file(filepath)

    if current_hash is None:

        return "File not found!"

    elif current_hash == original_hash:

        return "File Integrity VERIFIED"

    else:

        return "WARNING: File has been MODIFIED!"

# Main program loop
while True:

    print(Fore.CYAN + "\n=== Hash Generator & Integrity Monitor ===")

    print(Fore.YELLOW + "1. Generate MD5 Hash")
    print(Fore.YELLOW + "2. Generate SHA256 Hash")
    print(Fore.YELLOW + "3. Hash File")
    print(Fore.YELLOW + "4. Check File Integrity")
    print(Fore.YELLOW + "5. Exit")

    choice = input(Fore.WHITE + "Choose option: ")

    # MD5 Hash
    if choice == "1":

        text = input(
            Fore.WHITE +
            "Enter text: "
        )

        result = generate_md5(text)

        print(
            Fore.GREEN +
            f"\nMD5 Hash:\n{result}"
        )

        write_log(
            f"Generated MD5 Hash"
        )

    # SHA256 Hash
    elif choice == "2":

        text = input(
            Fore.WHITE +
            "Enter text: "
        )

        result = generate_sha256(text)

        print(
            Fore.GREEN +
            f"\nSHA256 Hash:\n{result}"
        )

        write_log(
            f"Generated SHA256 Hash"
        )

    # Hash File
    elif choice == "3":

        filepath = input(
            Fore.WHITE +
            "Enter file path: "
        )

        result = hash_file(filepath)

        if result:

            print(
                Fore.GREEN +
                f"\nFile SHA256 Hash:\n{result}"
            )

            write_log(
                f"Generated file hash for {filepath}"
            )

        else:

            print(
                Fore.RED +
                "\nCould not read file!"
            )

    # Integrity Check
    elif choice == "4":

        filepath = input(
            Fore.WHITE +
            "Enter file path: "
        )

        original_hash = input(
            Fore.WHITE +
            "Enter original hash: "
        )

        result = check_integrity(
            filepath,
            original_hash
        )

        # Verified
        if "VERIFIED" in result:

            print(
                Fore.GREEN +
                f"\n{result}"
            )

        # Modified
        else:

            print(
                Fore.RED +
                f"\n{result}"
            )

        write_log(result)

    # Exit
    elif choice == "5":

        print(Fore.CYAN + "Goodbye!")
        break

    # Invalid option
    else:

        print(
            Fore.RED +
            "\nInvalid choice!"
        )