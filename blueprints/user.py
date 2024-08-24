from flask import Blueprint

app = Blueprint("user", __name__)


@app.route('/user')
def user() -> object:  # put application's code here
    return 'user Page'

