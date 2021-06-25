# 1. import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

@app.route("/hazDane")
def hazdane():
    # set this up to call the predict module and pass it an image
    # path? url? download stream?
    return ""

if __name__ == "__main__":
    app.run(debug=True)
