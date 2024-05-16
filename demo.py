from flask import Flask

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    return "This is cool website"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)