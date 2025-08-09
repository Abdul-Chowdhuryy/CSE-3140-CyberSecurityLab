import os
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def load_public_key(key_path):
    """Loads the RSA public key from a given file."""
    with open(key_path, 'r') as key_file:
        return RSA.importKey(key_file.read())

def verify_signature(executable_path, signature_path, verifier):
    """Verifies whether the signature matches the executable."""
    with open(executable_path, 'rb') as exe_file:
        hashed_data = SHA256.new(exe_file.read())
    with open(signature_path, 'rb') as sig_file:
        signature = sig_file.read()
    return verifier.verify(hashed_data, signature)

def main():
    key = load_public_key('/home/cse/Lab3/Q3pk.pem')
    verifier = PKCS1_v1_5.new(key)  # RSA verifier
    directory = '/home/cse/Lab3/Q3files'
    
    for entry in os.scandir(directory):
        if entry.path.endswith('.sign'):
            exe_path = entry.path[:-5]  # Remove '.sign' to get executable path
            if verify_signature(exe_path, entry.path, verifier):
                print(f'Success: {exe_path}')
            else:
                print(f'Failure: {exe_path}')

if __name__ == "__main__":
    main()