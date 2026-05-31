import hashlib
from colorama import init, Fore
from datetime import datetime

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

# Generate SHA256 hash for file
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

# Create baseline
def save_baseline(filepath):

    file_hash = hash_file(filepath)

    if file_hash is None:

        return False

    with open("hash_database.txt", "a") as db:

        db.write(
            f"{filepath}|{file_hash}\n"
        )

    return True

# Verify file against baseline
def verify_baseline(filepath):

    current_hash = hash_file(filepath)

    if current_hash is None:

        return "File not found"

    try:

        with open("hash_database.txt", "r") as db:

            for line in db:

                saved_path, saved_hash = (
                    line.strip().split("|")
                )

                if saved_path == filepath:

                    if saved_hash == current_hash:

                        return "VERIFIED"

                    else:

                        return "MODIFIED"

        return "No baseline found"

    except:

        return "Database missing"

# Main program loop
while True:

    print(
        Fore.CYAN +
        "\n=== Hash Generator & Integrity Monitor ==="
    )

    print(Fore.YELLOW + "1. Generate MD5 Hash")
    print(Fore.YELLOW + "2. Generate SHA256 Hash")
    print(Fore.YELLOW + "3. Create File Baseline")
    print(Fore.YELLOW + "4. Verify File Integrity")
    print(Fore.YELLOW + "5. Exit")

    choice = input(
        Fore.WHITE +
        "Choose option: "
    )

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
            "Generated MD5 hash"
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
            "Generated SHA256 hash"
        )

    # Create Baseline
    elif choice == "3":

        filepath = input(
            Fore.WHITE +
            "Enter file path: "
        )

        if save_baseline(filepath):

            print(
                Fore.GREEN +
                "\nBaseline created successfully."
            )

            write_log(
                f"Baseline created for {filepath}"
            )

        else:

            print(
                Fore.RED +
                "\nFailed to create baseline."
            )

            write_log(
                f"Failed baseline creation for {filepath}"
            )

    # Verify Integrity
    elif choice == "4":

        filepath = input(
            Fore.WHITE +
            "Enter file path: "
        )

        result = verify_baseline(filepath)

        if result == "VERIFIED":

            print(
                Fore.GREEN +
                "\nFile Integrity VERIFIED"
            )

        elif result == "MODIFIED":

            print(
                Fore.RED +
                "\nWARNING: File Modified!"
            )

        else:

            print(
                Fore.YELLOW +
                f"\n{result}"
            )

        write_log(
            f"Integrity check: {filepath} -> {result}"
        )

    # Exit
    elif choice == "5":

        print(
            Fore.CYAN +
            "Goodbye!"
        )

        break

    # Invalid choice
    else:

        print(
            Fore.RED +
            "\nInvalid choice!"
        )