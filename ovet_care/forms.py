#!/usr/bin/python3
"""
This is a module that handles creation of forms using Python's WTF library
and Bootstrap
""" 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                                ValidationError)
from ovet_care.models import (Staff, User, Pet, PetBreed, PetType, Services,
                              Transactions)


class RegistrationForm(FlaskForm):
    """Class to create User Registration form"""
    firstname = StringField('First Name',
                                  validators=[DataRequired(),
                                              Length(min=2, max=32)],
                                  id='firstname', name='firstname')
    lastname = StringField('Last Name',
                                  validators=[DataRequired(),
                                              Length(min=2, max=32)],
                                  id='lastname', name='lastname')
    email = StringField('Email ID', validators=[DataRequired(),
                                                      Email()],
                        id='email', name='email')
    phone_num = StringField('Phone Number',
                            validators=[DataRequired(), Length(min=11,
                                                               max=11)],
                            id='phone_num', name='phone_num')
    password = PasswordField('Password', validators=[DataRequired(),
                                                      Length(min=6, max=20)],
                             id='password', name='password')
    password_confirm = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')],
                                     id='password_confirm',
                                     name='password_confirm')
    submit = SubmitField('Register')
    
    def validate_email(self, email):
        """This is an instance method that validates an email entered from the
        forms input fields"""
        user_email = User.query.filter_by(email=email.data).first()
        if user_email:
            raise ValidationError('The email provided is already taken.')
        
    def validate_phone_num(self, phone):
        """This is an instance method that validates a phone number
        entered from the forms input fields"""
        user_phone = User.query.filter_by(phone_num=phone.data).first()
        if user_phone:
            raise ValidationError('The phone number provided is already in use.')
    
    
class UserLoginForm(FlaskForm):
    """Class to create Login form"""
    email = StringField('Email ID', validators=[DataRequired(),
                                                      Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')    
  