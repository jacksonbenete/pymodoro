# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 00:49:59 2016

@author: Muhammad
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Criatura(db.Model):
    multiverseid = db.Column(db.String(), primary_key=True, unique=True)
    cmc = db.Column(db.Integer)
    colorIdentity = db.Column(db.String())
    name = db.Column(db.String())
    power = db.Column(db.String())
    toughness = db.Column(db.String())
    types = db.Column(db.String())
    subtypes = db.Column(db.String())
    
    def __init__(self, multiverseid, cmc, colorIdentity, name, power, toughness, types, subtypes):
        self.cmc = cmc
        self.colorIdentity = colorIdentity
        self.multiverseid = multiverseid
        self.name = name
        self.power = power
        self.subtypes = subtypes
        self.toughness = toughness
        self.types = types
        
    def __repr__(self):
        return '<Criatura %r>' % self.name
    