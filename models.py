"""Contains Project model class and associated code."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///projects.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column("Created", db.DateTime)
    title = db.Column("Title", db.String())
    description = db.Column("Description", db.Text)
    skills = db.Column("Skills Practiced", db.Text)
    url = db.Column("URL", db.Text)

    def __repr__(self):
        return f"""<Project (Title: {self.title}
                Created: {self.created}
                Description: {self.description}
                Skills Practiced: {self.skills}
                URL: {self.url}
                )"""
