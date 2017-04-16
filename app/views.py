from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, login_manager, db, bcrypt
from .forms import LoginForm
from .models import User, Metric, Record


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
# @login_required
def index():
    user = g.user
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
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        user = User.query.filter_by(email=form.email.data).first()
        # check credentials
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                remember_me = False
                if 'remember_me' in session:
                    remember_me = session['remember_me']
                    session.pop('remember_me', None)
                login_user(user, remember=remember_me)
                flash('Logged in successfully.')
                # next = flask.request.args.get('next')
                # if not is_safe_url(next):
                    # return flask.abort(400)
                return redirect(request.args.get('next') or url_for('index'))
            flash('Email or Password incorrect - try again')
            return redirect(url_for('login'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout', methods=["GET"])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))
