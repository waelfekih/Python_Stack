from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def hi(name):
    return f"Hi {name}"

@app.route("/say/<name>/<int:num>")
def nameRepeated(name, num):
    return f"Hi ,{name * num}"

if __name__ == "__main__":
    app.run(debug=True)
