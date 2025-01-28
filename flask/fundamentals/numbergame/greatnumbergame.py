from flask import Flask , render_template , session , request , redirect
import random

app = Flask(__name__)
app.secret_key= "wael"

@app.route("/")
def home():
    if "num" not in session:
        session['num'] = random.randint(1,100)

    return render_template("greatnumbergame.html")

@app.route("/guess" ,methods=['post'])
def guess():
    session['a'] = int(request.form['a'])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)