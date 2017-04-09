from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Billy'}  # fake user
    metrics = [
        {
            'name': 'Skipping',
            'text': 'daily skipping record'
        },
        {
            'name': 'Chinese',
            'text': 'daily chinese practise'
        }
    ]
    return render_template('index.html', title='Home', user=user, metrics=metrics)
