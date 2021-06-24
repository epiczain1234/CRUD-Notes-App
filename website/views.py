from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# when this route is hit, the function below is returned
@views.route('/')
def home():
    return render_template("home.html")