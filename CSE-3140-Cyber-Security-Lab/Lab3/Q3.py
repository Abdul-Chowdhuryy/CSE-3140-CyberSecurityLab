import os
import subprocess

def compute_hash(file_name):
    # Computes the SHA-256 hash of a given file
    os.chdir('/home/cse/Lab3/Q2files')
    output = subprocess.run(['sha256sum', file_name], stdout=subprocess.PIPE)
    hash_value = output.stdout.split()
    return hash_value

def main():
    executables = [f for f in os.listdir('/home/cse/Lab3/Q2files') if f.endswith('.exe')]  # Get all .exe files
    os.chdir('/home/cse/Lab3')
    with open('Q2hash.txt', 'r') as hash_file:
        expected_hash = hash_file.read().strip()  # Read expected hash
    
    for exe in executables:
        computed_hash, exe_name = compute_hash(exe)
        if computed_hash == expected_hash.encode():  # Ensure proper comparison
            print(f"Match found: {exe_name.decode()}")

if __name__ == "__main__":
    main()