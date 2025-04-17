from flask import render_template, request, redirect, url_for
from .models import db, Task

def init_app(app):
    @app.route('/')
    def index():
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)
    
    @app.route('/add', methods=['POST'])
    def add_task():
        content = request.form['content']
        new_task = Task(content=content)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    
    @app.route('/delete/<int:id>')
    def delete_task(id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))
    
    @app.route('/toggle/<int:id>')
    def toggle_task(id):
        task = Task.query.get_or_404(id)
        task.done = not task.done
        db.session.commit()
        return redirect(url_for('index'))