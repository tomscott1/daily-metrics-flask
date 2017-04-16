from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, login_manager, db
from .forms import LoginForm
from .models import User, Metric, Record

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


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
# potentially need to tell login_manager this is the login function....
def login():
    if g.user is not None and g.users.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # check credentials
        User.
        session['remember_me'] = form.remember_me.data
        login_user(user)
        flash('Logged in successfully.')
        next = flask.request.args.get('next')
                # flash('Login requested for remember_me="%s", email="%s", password="%s"' %
                #       (str(form.remember_me.data), form.email.data, form.password.data))
        if not is_safe_url(next):
            return flask.abort(400)
        return redirect('/index')
    return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
