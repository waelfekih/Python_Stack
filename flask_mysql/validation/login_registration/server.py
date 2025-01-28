from flask import Flask , render_template , redirect
app =Flask( __name__)
from flask_app.controllers import Loginregister
from flask_app.models.loginregister import Loginregister
from flask_app import app



if __name__ == "__main__":
    app.run(debug=True)