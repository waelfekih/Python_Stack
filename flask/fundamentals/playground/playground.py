from flask import Flask , render_template , redirect

app = Flask(__name__)

@app.route("/play")
def threeboxes():
    return render_template("playground.html" , box = 3, color="blue")

@app.route("/")
def wael():
    return redirect("/play")

@app.route("/play/<int:x>")
def numbox(x): 
    return render_template("playground.html" , box = x, color = "blue")

@app.route("/play/<int:x>/<string:color>")
def color(x , color):
    return render_template("playground.html" , box=x , color=color)

    





if __name__ == "__main__":
    app.run(debug=True)
