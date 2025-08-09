from flask import Flask

app = Flask(__name__)

@app.route('/')
def website():
    return """
    <html>
        <head><title>Husky Banking</title></head>
        <body style="font-family: Arial; text-align: center; padding-top: 50px;">
            <h1>Welcome to Husky Banking</h1>
            <p>Team 6</p>
            <p>Created by Abdul Chowdhury</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
