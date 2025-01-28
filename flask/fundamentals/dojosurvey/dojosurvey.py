from flask import Flask, render_template, session , redirect , request

app = Flask(__name__)

app.secret_key="wael"

@app.route('/')
def home():
    return render_template("dojosurvey.html")


@app.route('/process' , methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')
    
    



if __name__ == "__main__":
    app.run(debug=True)