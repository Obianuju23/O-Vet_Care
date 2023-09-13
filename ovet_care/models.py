#!/usr/bin/python3
"""
This is a module that creates Our Databases for the O-Vet Care Web application
"""
from datetime import datetime as dt
from ovet_care import db, login_manager
from flask_login import UserMixin


class Staff(db.Model, UserMixin):
    """This is a class to create the Staff database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    st_id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    is_active = db.Column(db.Integer, nullable=False, default=0)
    avatar = db.Column(db.String(20), nullable=False, default='default.png')

    def __repr__(self):
        '''Representation of the Staff class when an instance is displayed'''
        return f'Staff("{self.st_id}", "{self.email}", "{self.is_active}")'


class User(db.Model, UserMixin):
    """This is a class to create the User database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    u_id = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(32), nullable=False)
    lastname = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_num = db.Column(db.String(11), unique=True, nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default='default.png')
    created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    is_active = db.Column(db.Integer, nullable=False, default=0)
    pets = db.relationship('Pet', backref='owner', lazy=True)

    def __repr__(self):
        '''Representation of the User class when an instance is displayed'''
        return f'User("{self.u_id}", "{self.email}", "{self.created}")'


@login_manager.user_loader
def load_user(user_id):
    """a decorative function to load a user's details"""
    return User.query.get(int(user_id))


class PetType(db.Model, UserMixin):
    """This is a class to create the PetType database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    pt_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        '''Representation of the PetType class when an instance is called'''
        return f'Pet Type("{self.pt_id}", "{self.name}")'


class PetBreed(db.Model, UserMixin):
    """This is a class to create the PetBreed database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    pb_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.Integer, db.ForeignKey('pet_type.pt_id'), nullable=False)

    def __repr__(self):
        '''Representation of the PetBreed class when an instance is called'''
        return f'Pet Breed("{self.pb_id}", "{self.name}")'


class Pet(db.Model, UserMixin):
    """This is a class to create the Pet database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    p_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    pet_owner = db.Column(db.Integer, db.ForeignKey('user.u_id'), nullable=False)
    pet_type = db.Column(db.Integer, db.ForeignKey('pet_type.pt_id'), nullable=False)
    pet_breed = db.Column(db.Integer, db.ForeignKey('pet_breed.pb_id'), nullable=False)
    
    def __repr__(self):
        '''Representation of the Pet class when an instance is called'''
        return f'Pet("{self.p_id}", "{self.name}")'
    
    
class Services(db.Model, UserMixin):
    """This is a class to create the Services database using Python's Flask
    SQLAlchemy ORM using the db.model module"""
    s_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Float, nullable=False, default=0.0)
    
    def __repr__(self):
        '''Representation of the Services class when an instance is called'''
        return f'Services("{self.s_id}", "{self.name}", "{self.cost}")'
    

class Transactions(db.Model, UserMixin):
    """This class creates the Transactions database using Python's
    Flask SQLAlchemy ORM using the db.model module"""
    tran_id = db.Column(db.Integer, primary_key=True, nullable=False)
    tran_p_owner = db.Column(db.Integer, db.ForeignKey('user.u_id'),
                             nullable=False)
    tran_service = db.Column(db.Integer, db.ForeignKey('services.s_id'),
                             nullable=False)
    tran_on_pet = db.Column(db.Integer, db.ForeignKey('pet.p_id'),
                            nullable=False)
    tran_date = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    tran_status = db.Column(db.Integer, nullable=False, default=0)
    
    def __repr__(self):
        '''Representation of the Transaction class when an instance is
        called'''
        return f'Transaction("{self.tran_id}", "{self.tran_status}","{self.tran_date}")'
