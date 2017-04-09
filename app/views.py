from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


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
    return render_template('index.html', title='Home', user=user,
                           metrics=metrics)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for remember_me="%s", email="%s", password="%s"' %
              (str(form.remember_me.data), form.email.data, form.password.data))
        return redirect('/index')
    return render_template('login.html', title='Sign in', form=form)
