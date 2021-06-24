from flask import Blueprint

views = Blueprint('views', __name__)

# when this route is hit, the function below is returned
@views.route('/')
def home():
    return 'hello world'