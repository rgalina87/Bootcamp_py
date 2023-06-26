import flask

from . import forms, models
from . import app, db


@app.route('/', methods=['GET', 'POST'])
def index():

    form = forms.Todo()
    if flask.request.method == 'POST':
        task_content = flask.request.form['content']
        new_task = models.Todolist(to_do=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return flask.redirect('/')
        except:
            return "Error to add a task"
    else:
        tasks = models.Todolist.query.all()
        return flask.render_template("index.html", tasks=tasks, form=form)

@app.route('/done/int:<id>')
def done(id):
    pass


@app.route('/complete/<int:id>')
def complete(id):
    task_content = models.Todolist.query.filter_by(id).first()
    task_content.complete = False
    db.session.commit()
    return flask.redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    task_delete = models.Todolist.query.get_or_404(id)

    try:
        db.session.delete(task_delete)
        db.session.commit()
        return flask.redirect('/')
    except:
        return "Error"