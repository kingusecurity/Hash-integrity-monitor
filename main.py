import hashlib
import os
from colorama import init, Fore
from datetime import datetime

# Initialize colorama
init(autoreset=True)

DATABASE_FILE = "hash_database.txt"
LOG_FILE = "hash_log.txt"


# Logging Function
def write_log(message):

    with open(LOG_FILE, "a") as log_file:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        log_file.write(
            f"[{timestamp}] {message}\n"
        )


# Generate MD5 Hash
def generate_md5(text):

    return hashlib.md5(
        text.encode()
    ).hexdigest()


# Generate SHA256 Hash
def generate_sha256(text):

    return hashlib.sha256(
        text.encode()
    ).hexdigest()


# Hash File
def hash_file(filepath):

    sha256 = hashlib.sha256()

    try:

        with open(filepath, "rb") as file:

            while chunk := file.read(4096):

                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception:

        return None


# Create Directory Baseline
def create_directory_baseline(folder):

    try:

        with open(DATABASE_FILE, "w") as db:

            for root, dirs, files in os.walk(folder):

                for file in files:

                    filepath = os.path.join(
                        root,
                        file
                    )

                    file_hash = hash_file(
                        filepath
                    )

                    if file_hash:

                        db.write(
                            f"{filepath}|{file_hash}\n"
                        )

        return True

    except Exception:

        return False


# Verify Directory Integrity
def verify_directory(folder):

    try:

        baseline = {}

        with open(DATABASE_FILE, "r") as db:

            for line in db:

                path, saved_hash = (
                    line.strip().split("|")
                )

                baseline[path] = saved_hash

        changes = []

        current_files = set()

        for root, dirs, files in os.walk(folder):

            for file in files:

                filepath = os.path.join(
                    root,
                    file
                )

                current_files.add(
                    filepath
                )

                current_hash = hash_file(
                    filepath
                )

                if filepath in baseline:

                    if (
                        current_hash
                        != baseline[filepath]
                    ):

                        changes.append(
                            f"MODIFIED: {filepath}"
                        )

                else:

                    changes.append(
                        f"NEW FILE: {filepath}"
                    )

        for saved_file in baseline:

            if saved_file not in current_files:

                changes.append(
                    f"DELETED: {saved_file}"
                )

        return changes

    except Exception:

        return None


# Main Program
while True:

    print(
        Fore.CYAN +
        "\n=== Directory Integrity Monitor ==="
    )

    print(
        Fore.YELLOW +
        "1. Generate MD5 Hash"
    )

    print(
        Fore.YELLOW +
        "2. Generate SHA256 Hash"
    )

    print(
        Fore.YELLOW +
        "3. Create Directory Baseline"
    )

    print(
        Fore.YELLOW +
        "4. Verify Directory Integrity"
    )

    print(
        Fore.YELLOW +
        "5. Exit"
    )

    choice = input(
        Fore.WHITE +
        "Choose option: "
    )

    # MD5
    if choice == "1":

        text = input(
            "Enter text: "
        )

        result = generate_md5(text)

        print(
            Fore.GREEN +
            f"\nMD5:\n{result}"
        )

        write_log(
            "Generated MD5 hash"
        )

    # SHA256
    elif choice == "2":

        text = input(
            "Enter text: "
        )

        result = generate_sha256(text)

        print(
            Fore.GREEN +
            f"\nSHA256:\n{result}"
        )

        write_log(
            "Generated SHA256 hash"
        )

    # Create Baseline
    elif choice == "3":

        folder = input(
            "Enter folder path: "
        )

        if create_directory_baseline(
            folder
        ):

            print(
                Fore.GREEN +
                "\nBaseline created successfully."
            )

            write_log(
                f"Created baseline for {folder}"
            )

        else:

            print(
                Fore.RED +
                "\nFailed to create baseline."
            )

    # Verify
    elif choice == "4":

        folder = input(
            "Enter folder path: "
        )

        changes = verify_directory(
            folder
        )

        if changes is None:

            print(
                Fore.RED +
                "\nVerification failed."
            )

        elif len(changes) == 0:

            print(
                Fore.GREEN +
                "\nNo changes detected."
            )

        else:

            print(
                Fore.RED +
                "\nChanges Found:\n"
            )

            for change in changes:

                print(change)

                write_log(change)

    # Exit
    elif choice == "5":

        print(
            Fore.CYAN +
            "Goodbye!"
        )

        break

    else:

        print(
            Fore.RED +
            "\nInvalid choice!"
        )