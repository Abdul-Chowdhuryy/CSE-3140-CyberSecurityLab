import os
from Crypto.PublicKey import RSA

# Generate a 2048-bit RSA key pair
print("Generating RSA key pair...")
private_key = RSA.generate(2048)  # Generate 2048-bit key pair

# Export the private and public keys
private_key_bytes = private_key.export_key()  # Private key in bytes
public_key_bytes = private_key.publickey().export_key()  # Public key in bytes

# Define the directory path
key_directory = '/home/cse/Lab3/Q6files/Solutions/'

# Ensure the directory exists
os.makedirs(key_directory, exist_ok=True)
print(f"Directory {key_directory} ensured")

# Write the keys to the specified files in the directory
with open(os.path.join(key_directory, 'e.key'), "wb") as public_key_file:
    public_key_file.write(public_key_bytes)
    print("Public key saved to e.key")

with open(os.path.join(key_directory, 'd.key'), 'wb') as private_key_file:
    private_key_file.write(private_key_bytes)
    print("Private key saved to d.key")