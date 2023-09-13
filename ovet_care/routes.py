#!/usr/bin/python3
"""
This is a module that creates routes for the O-Vet Care Web application
"""
from flask import render_template, url_for, redirect, flash, request
from ovet_care import app, db, bcrypt
from ovet_care.forms import RegistrationForm, UserLoginForm
from ovet_care.models import User
from flask_login import login_user, current_user


"""This is the route to the index or Landing page"""
@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Function to route to the home page when the / route is hit"""
    return render_template('index.html', title="Home")


"""This is the route to the about page"""
@app.route('/about', methods=['GET'], strict_slashes=False)
def about():
    """Function to route to the about page when the /about route is hit"""
    return render_template('about.html', title="About")


"""This is the route to the service page"""
@app.route('/service', methods=['GET'], strict_slashes=False)
def service():
    """Function to route to the service page when the /service route is hit"""
    return render_template('service.html', title="Services")


"""This is the route to the contact page"""
@app.route('/contact', methods=['GET'], strict_slashes=False)
def contact():
    """Function to route to the contact page when the /contact route is hit"""
    return render_template('contact.html', title="Contact")


"""This is the route to the register page"""
@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """Function to route to the register page when the /register route is
    hit"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data.title(),
                    lastname=form.lastname.data.title(),
                    email=form.email.data.lower(),
                    phone_num=form.phone_num.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration was successful', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


"""This is the route to the login page"""
@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Function to route to the login page when the /login route is hit"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login was not successful. Invalid email/password.', 'danger')
    return render_template('login.html', title="Login", form=form)
