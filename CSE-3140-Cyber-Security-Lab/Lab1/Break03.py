import hashlib
import subprocess
import time

MEA = 60

def my_hash(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    string_hash = sha256.hexdigest()
    return string_hash

def hash_lookup(hashed_pw, hashed_pw_dict):
    return hashed_pw in hashed_pw_dict

def login(username, password):
    result = subprocess.run(
        ["python3", "Login.pyc", username, password],
        capture_output=True,
        text=True,
        cwd="/home/cse/Lab1/Q5/"
    )
    if result.stdout == "Login successful.\n":
        print(result.stdout.strip())
        print(f"Username '{username}': Password '{password}'")
        end = time.time()
        print(f"Time taken to find gang member: {end - start}")
        print()
        return True
    return False

def find_password(passwords, hashed_pw_dict, start):
    measurement = 0
    successes = []

    for i, password in enumerate(passwords):
        if time.time() - start > measurement:
            print(f'On attempt {i}/{len(passwords)}, {(time.time() - start) // 60} minutes have passed')
            measurement += MEA

        for digit1 in range(10):
            for digit2 in range(10):
                new_pw = password + str(digit1) + str(digit2)
                hashed_pw = my_hash(new_pw)

                if hash_lookup(hashed_pw, hashed_pw_dict):
                    username = hashed_pw_dict[hashed_pw]
                    if login(username, new_pw):
                        print(f'Success: {username} {password}')
                        successes.append(f'Success: {username} {password}')
                        return successes
    return successes

if __name__ == "__main__":
    start = time.time()
    print("Running Program")
    print("Searching for passwords...")
    print("\nProgram start time: {start - start}")
    
    with open("/home/cse/Lab1/Q5/PwnedPWs100k") as f:
        pwnedpws = [line.rstrip('\n') for line in f]

    with open("/home/cse/Lab1/Q5/HashedPWs") as f:
        hashedpws = [line.rstrip('\n') for line in f]

    hashdict = {}
    for line in hashedpws:
        username, password = line.split(",")
        hashdict[password] = username

    result = find_password(pwnedpws, hashdict, start)
    print(result)

    if len(result) == 0:
        print("No Successful Login Attempts")

    end = time.time()
    print(f"\nProgram End Time: {end - start}")