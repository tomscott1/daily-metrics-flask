from flask import render_template, flash, redirect, session, url_for
from flask import request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, login_manager, db, bcrypt
from .forms import LoginForm, RegisterForm, NewMetricForm
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
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('index.html', title='Home', user=g.user,
                           metrics=metrics, logged_in=g.user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('home'))
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
                return redirect(request.args.get('next') or url_for('home'))
            flash('Email or Password incorrect - try again')
            return redirect(url_for('login'))
    return render_template('login.html', title='Log in', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if not db.session.query(db.exists().where(
                User.email == form.email.data)).scalar():
            new_user = User(email=form.email.data,
                            password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('User successfully registered')
            return redirect(request.args.get('next') or url_for('index'))
        flash('Email already exists - please choose another email')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    # get metrics for user
    metrics = db.session.query(Metric).filter_by(user_id = g.user.id)
    return render_template('home.html', title='Home', user=g.user,
                           logged_in=True, metrics=metrics)


@app.route('/add_metric', methods=['GET', 'POST'])
@login_required
def add_metric():
    form = NewMetricForm()
    if form.validate_on_submit():
        new_metric = Metric(user_id=g.user.id, name=form.name.data,
                            is_bool=form.is_bool.data,
                            max_val=form.max_val.data,
                            min_val=form.min_val.data, increment=1)
        db.session.add(new_metric)
        db.session.commit()
        flash('New Metric Added')
        return redirect(request.args.get('next') or url_for('home'))
    return render_template('add_metric.html', title='Add Metric',
                           logged_in=True, user=g.user, form=form)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
