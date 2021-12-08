"""Contains Project model class and associated code."""

from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_basec
import datetime

 

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.sqlite3'

db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.Date, default=datetime.datetime.now)
    title = db.Column('Title', db.String(), unique=True)
    url = db.Column('URL', db.String())
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)

    def __repr__(self):
        return f'''<Project (Title: {self.title}
        Description: {self.description}
        Skills: {self.skills}
        Created: {self.created}
        URL: {self.url}
        '''
