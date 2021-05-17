from app import app, db
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime

import models
import forms

# We can point multiple adresses to the same route/file
@app.route('/')
@app.route('/index')
def index():
    tasks = models.Task.query.all()
    return render_template('index.html', tasks=tasks) # by feeding a "tasks" variable to render_template(), we can pass information to the target file (html)


@app.route('/add', methods=['GET', 'POST']) # We have to enable additional methods if we want e.g. to be able to POST at some address
def add():
    form = forms.AddTaskForm()
    # check if the form was submitted and approved as containing a valid input
    if form.validate_on_submit():
        task = models.Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()
        flash('Task added')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


# using '<int:task_id>' allows us to extract information from the URL to be used in our code
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    form = forms.AddTaskForm()
    task = models.Task.query.get(task_id)
    print(task)
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            # We do not have to add a new db entry as we are editing an already existing one
            db.session.commit()
            flash('Task updated') # this will create a text prompt informing the user about what operations have been performed
            return redirect(url_for('index')) # redirect the user to the index homepage after she has finished editing her task
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    flash(f'Task with id {task_id} does not exit.')
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    form = forms.DeleteTaskForm()
    task = models.Task.query.get(task_id) # get the task id from the database
    if task:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(task)
                db.session.commit()
                flash('Task deleted')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    flash(f'Task with id {task_id} does not exit.')
    return redirect(url_for('index'))
