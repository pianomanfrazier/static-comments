#!venv/bin/python

from app import app, db
from app.models import Comment

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Comment': Comment}
