import hashlib
import subprocess
import time

def generate_sha256_hash(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()

def attempt_login(username, password):
    result = subprocess.run(
        ["python3", "Login.pyc", username, password],
        capture_output=True,
        text=True,
        cwd="/home/cse/Lab1/Q6/"
    )
    if result.stdout == "Login successful.\n":
        print(result.stdout.strip())
        print(f"Username '{username}': Password '{password}'")
        end = time.time()
        print(f"Time taken to find user credentials: {end - start}")
        print()
        return True
    return False

def find_valid_password(username, password_list, user_salt_map, user_password_map, output_filepath):
    target_password_hash = user_password_map[username]
    salt = user_salt_map[username]

    for password in password_list:
        for digit in range(10):
            generated_password = str(salt) + password + str(digit)
            test_password = password + str(digit)

            print(f'Attempting: {generated_password}')
            hashed_password = generate_sha256_hash(generated_password)

            if hashed_password == target_password_hash:
                if attempt_login(username, test_password):
                    with open(output_filepath, "a") as output_file:
                        output_file.write(f"Username: {username}, Password: {test_password}\n")
                    return True
    return False

def get_common_elements(list1, list2):
    return list(set(list1) & set(list2))

if __name__ == "__main__":
    start = time.time()
    print("Running Password Recovery Script")
    print("Searching for valid credentials...")
    print("\nProgram start time: {start - start}")

    output_filepath = "/home/cse/discovered_passwords.txt"

    with open("/home/cse/Lab1/Q6/PwnedPWs100k") as file:
        password_list = [line.rstrip('\n') for line in file]

    with open("/home/cse/Lab1/Q6/SaltedPWs") as file:
        salted_passwords = [line.rstrip('\n') for line in file]

    with open("/home/cse/Lab1/Q6/gang") as file:
        gang_list = [line.rstrip('\n') for line in file]

    user_salt_map = {}
    user_password_map = {}

    for entry in salted_passwords:
        username, salt, hashed_password = entry.split(",")
        user_salt_map[username] = salt
        user_password_map[username] = hashed_password

    gang_members = list(user_salt_map.keys())
    common_users = get_common_elements(gang_members, gang_list)

    with open(output_filepath, "w") as output_file:
        output_file.write("Discovered Passwords:\n")

    login_successful = False
    for user in common_users:
        if find_valid_password(user, password_list, user_salt_map, user_password_map, output_filepath):
            login_successful = True
            break

    if not login_successful:
        print("No successful login attempts.")
    
    end = time.time()
    print(f"\nProgram End Time: {end - start}")