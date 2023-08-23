from ovet_care import app
from flask import url_for, render_template, request

"""This is the route to the index or Landing page"""
@app.route('/', methods=['GET'], strict_slashes=False)
@app.route('/home', methods=['GET'], strict_slashes=False)
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
