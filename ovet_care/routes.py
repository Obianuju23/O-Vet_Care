#!/usr/bin/python3
"""
This is a module that creates routes for the O-Vet Care Web application
"""
from flask import url_for, render_template, request, redirect, flash
from ovet_care import app
from ovet_care.forms import RegistrationForm, UserLoginForm
from ovet_care.models import Staff, User, Pet, PetType, PetBreed


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

"""This is the route to the login page"""
@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Function to route to the login page when the /login route is hit"""
    form = UserLoginForm()
    if form.validate_on_submit():
        flash('Login was successful', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title="Login", form=form)

"""This is the route to the register page"""
@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """Function to route to the register page when the /register route is
    hit"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Registration was successful', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', title="Register", form=form)
