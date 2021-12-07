"""An interface for a portfolio web application.
The main (index) page lists your projects including the project title and short
description. Each project links to a detail page that displays the title, date,
and description.
The application lets the user add or edit project information. When adding or
editing a project, the application prompts the user for title, date, skills,
description, and a link to a repo. The results for these entries are stored in
a database and displayed on the homepage.
"""
from flask import Flask, render_template, url_for, request, redirect, send_file
from models import db, Project, app
from time import sleep
import datetime


@app.route('/')
def index():
    """Portfolio Homepage"""
    all_projects = Project.query.all()
    return render_template('index.html', projects=all_projects)


@app.route("/about")
def about():
    """Mason's About Page"""
    all_projects = Project.query.all()
    return render_template("about.html", projects=all_projects)


@app.route('/projects/<id>')
def detail(id):
    """Return the details of a project"""
    all_projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html', projects=all_projects, project=project)

@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    """Add a new project to the portfolio"""
    all_projects = Project.query.all()
    if request.form:
        new_project = Project(created=datetime.datetime.strptime(request.form['date'], "%Y-%m"),
                              title=request.form['title'],
                              description=request.form['desc'],
                              skills=request.form['skills'],
                              url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=all_projects)


@app.route("/project/<id>/edit", methods=['GET', 'POST'])
def edit_project(id):
    """Edit a Project"""
    all_projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.created = datetime.datetime.strptime(
            request.form['date'], "%Y-%m")
        project.title = request.form['title']
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.url = request.form['github']
        db.session.commit()
        print(project)
        return redirect(url_for('index'))
    return render_template('edit.html', projects=all_projects, project=project)


@app.route("/projects/<id>/delete", methods=['GET', 'POST'])
def delete(id):
    """Delete a Project."""
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))


@app.errorhandler(404)
def not_found(error):
    """404 Error Page."""
    portfolio = Project.query.all()
    return render_template("404.html", msg=error), 404


# adapted from https://stackoverflow.com/questions/24577349/flask-download-a-file
@app.route('/download')
def downloadFile():
    """Display Mason CV"""
    path = "masonbcoding_CV.pdf"
    return send_file(path, as_attachment=True)
# end adaptation



if __name__ == '__main__':
    db.create_all()
    project1 = Project(
        title="Number Guessing Game",
        created=datetime.datetime(2020, 4, 19),
        description="""
                        \nPython TechDegree First Project Number Guessing Game""",
        skills="Python",
        url="https://github.com/masonbcoding/python-techdegree-project-1")

    project2 = Project(
        title="Basketball Stats Tool",
        created=datetime.datetime(2020, 10, 2),
        description="""
                        \nSecond Project: Basketball Stat Tracker and Team Organizer""",
        skills="Python",
        url="https://github.com/masonbcoding/python_techdegree_project_2")

    project3 = Project(
        title="Phrase Hunter",
        created=datetime.datetime(2020, 11, 7),
        description="""
                        \nThird Project: Console Guessing Game""",
        skills="Python",
        url="https://github.com/masonbcoding/techdegree-project-3-phrase-hunter")

    project4 = Project(
        title="A Store Inventory",
        created=datetime.datetime(2021, 11, 30),
        description="""
                        \nFourth Project: Store Inventory Management Tool""",
        skills="Python",
        url="https://github.com/masonbcoding/techdegree-project4-a-store-inventory")


    db.session.add(project1)
    db.session.commit()
    app.run(debug=True, port=8000, host='0.0.0.0')
    app.run(debug=True, port=8000, host='127.0.0.1')
