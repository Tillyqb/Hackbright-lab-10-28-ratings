"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import * # StrictUndefined



app = Flask(__name__)
app.secret_key = "poij;lkrjaf;"
app.jinja_env.undefined = StrictUndefined
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

# Replace this with routes and view functions!


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
