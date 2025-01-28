from flask import Flask , render_template , session , redirect

app = Flask(__name__)
app.secret_key = "wael"

@app.route("/")
def visit():
    if 'views' not in session:
        session["views"] = 0

    session["views"] += 1
    return render_template('counter.html' , count=session["views"]) 


@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)