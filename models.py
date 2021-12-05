"""Contains Project model class and associated code."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


class Project(db.Model):
    """Model class for adding and editing project information."""

    __tablename__ = "project"

    id = db.Column("ID", db.Integer, primary_key=True)
    title = db.Column("Title", db.String())
    date_completed = db.Column("Date", db.Date)
    description = db.Column("Description", db.String())
    skills = db.Column("Skills Practiced", db.String())
    github = db.Column("GitHub Repo", db.String())

    def __repr__(self):
        """Return printable representation of Project."""
        return f"""\n----------
                \rProject ID: {self.id}
                \r----------
                \Project Title: {self.title}
                \r----------
                \Date Completed: {self.date_completed}
                \r----------
                \Description: {self.description}
                \r----------
                \Skills practiced: {self.skills_practiced}
                \r----------
                \rGithub Repo: {self.github}
                \r----------\n"""
