from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "I am using a debugger"

@app.about("/about")
def about():
    return "Thanos"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001 ,debug=True)