from flask import Flask , render_template

tab = Flask(__name__)


@tab.route("/")
def table():
    return render_template("HTMLtable.html")


if __name__ == "__main__":
    tab.run(debug=True)