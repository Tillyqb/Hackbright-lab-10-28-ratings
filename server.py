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

    return render_template('/homepage.html')

@app.route('/movies')
def movies():
    """View all movies"""

    all_movies = crud.display_movies()
    return render_template('/all_movies.html',
                            movies = all_movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)


# Replace this with routes and view functions!


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
