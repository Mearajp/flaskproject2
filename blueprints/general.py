from flask import Blueprint

app = Blueprint("general", __name__)


@app.route('/')
def Main():  # put application's code here
    return 'Main Page'

@app.route('/About')
def About():  # put application's code here
    return 'About us'

