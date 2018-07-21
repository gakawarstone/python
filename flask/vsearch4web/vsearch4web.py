from flask import Flask
from vsearch import search4letters
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4', methods=['post'])
def do_search() -> str:
    return str(search4letters('life, the universe, and everything'))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


app.run(debug=True)
