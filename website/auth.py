from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", text="Test", boolean=False)

@auth.route('/logout')
def logout():
    return "logged out"

@auth.route('/sign-up')
def signup():
    return render_template("signup.html")