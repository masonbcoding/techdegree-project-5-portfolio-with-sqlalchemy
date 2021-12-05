"""An interface for a portfolio web application.
The main (index) page lists your projects including the project title and short
description. Each project links to a detail page that displays the title, date,
and description.
The application lets the user add or edit project information. When adding or
editing a project, the application prompts the user for title, date, skills,
description, and a link to a repo. The results for these entries are stored in
a database and displayed on the homepage.
"""
from flask import render_template, url_for, request, redirect
from models import db, Project, app
import datetime


@app.route("/")
def portfolio_index():
    """Portfolio homepage/index."""
    portfolio = Project.query.all()
    return render_template("index.html", portfolio=portfolio)


@app.route("/about")
def about_author():
    """Display author's about page."""
    portfolio = Project.query.all()
    return render_template("about.html", portfolio=portfolio)


@app.route("/project/<id>")
def project_details(id):
    """Display details of a project."""
    portfolio = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template("detail.html", project=project, portfolio=portfolio)


@app.route("/project/new", methods=['GET', 'POST'])
def new_project():
    """Add a new project."""
    portfolio = Project.query.all()
    if request.form:
        split_month_and_year = request.form["date"].split("-")
        year = int(split_month_and_year[0])
        month = int(split_month_and_year[1])
        day = int(request.form["day"])
        new_project = Project(title=request.form["title"],
                              date_completed=datetime.datetime(year,
                              month, day),
                              description=request.form["description"],
                              skills=request.form["skills"],
                              github=request.form["github"])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("portfolio_index"))
    return render_template("projectform.html", portfolio=portfolio)


@app.route("/project/<id>/edit", methods=['GET', 'POST'])
def edit_project(id):
    """Edit a project."""
    portfolio = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        split_month_and_year = request.form["date"].split("-")
        year = int(split_month_and_year[0])
        month = int(split_month_and_year[1])
        day = int(request.form["day"])
        project.title = request.form["title"]
        project.date_completed = datetime.datetime(year, month, day)
        project.description = request.form["description"]
        project.skills = request.form["skills"]
        project.github = request.form["github"]
        db.session.commit()
        return redirect(url_for("portfolio_index"))
    return render_template("editform.html", project=project, portfolio=portfolio)


@app.route("/projects/<id>/delete", methods=['GET', 'POST'])
def delete_project(id):
    """Delete a project."""
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("portfolio_index"))


@app.errorhandler(404)
def not_found(error):
    """Display 404 error page."""
    portfolio = Project.query.all()
    return render_template("404.html", msg=error, portfolio=portfolio), 404


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")
