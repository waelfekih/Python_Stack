from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.post import Post

@app.route("/comment", methods=["POST"])
def create_post():
    print("in create route")
    print(request.form)
    Post.create_com(request.form)
     
    return redirect("/wall")

@app.route("/comment/delete/<post_id>")
def delete_post(post_id):
    Post.delete(post_id)
    return redirect("/wall")

