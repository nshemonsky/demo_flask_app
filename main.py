from flask import Flask
app = application = Flask(__name__)

@app.route("/")
def hello():
    return "Hello ReactiveOps!"

if __name__ == "__main__":
    app.run()
