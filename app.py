"""An interface for a portfolio web application.
The main (index) page lists your projects including the project title and short
description. Each project links to a detail page that displays the title, date,
and description.
The application lets the user add or edit project information. When adding or
editing a project, the application prompts the user for title, date, skills,
description, and a link to a repo. The results for these entries are stored in
a database and displayed on the homepage.
"""


from flask import render_template, redirect, url_for, request
from models import db, Project, app
import datetime


@app.route('/')
def index():
    all_projects = Project.query.all()
    return render_template('index.html', projects=all_projects)


@app.route('/about')
def about():
    all_projects = Project.query.all()
    return render_template('about.html', projects=all_projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def new():
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


@app.route('/projects/<id>')
def detail(id):
    all_projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html', projects=all_projects, project=project)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
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


@app.route('/project/<id>/delete')
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", msg=error), 404


if __name__ == '__main__':
    db.create_all()
    project_1 = Project(
        title = 'python-techdegree-project-1',
        created = datetime.date(2019, 4, 10), 
        skills = 'Python', 
        url = 'https://github.com/masonbcoding/python-techdegree-project-1', 
        description = '''
            Number Guessing Game
        ''')

    project_2 = Project(
        title = 'python_techdegree_project_2',
        created = datetime.date(2020, 10, 2), 
        skills = 'Python', 
        url = 'https://github.com/masonbcoding/python_techdegree_project_2', 
        description = '''
            Basketball Team Stats Tool
        ''')

    project_3 = Project(
        title = 'techdegree-project-3-phrase-hunter',
        created = datetime.date(2020, 11, 7), 
        skills = 'Python', 
        url = 'https://github.com/masonbcoding/techdegree-project-3-phrase-hunter', 
        description = '''
            Phrase Hunter Game
        ''')

    project_4 = Project(
        title = 'techdegree-project4-a-store-inventory',
        created = datetime.date(2021, 11, 29), 
        skills = 'Python', 
        url = 'https://github.com/masonbcoding/techdegree-project4-a-store-inventory', 
        description = '''
            Store Inventory Project
        ''')


    #db.session.add(project_1)
    #db.session.add(project_2)
    #db.session.add(project_3)
    #db.session.add(project_4)
    #db.session.commit()
    app.run(debug=True, port=8000, host='127.0.0.1')
