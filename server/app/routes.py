from app import app
from flask import render_template
from .authentication import requires_auth

@app.route('/')
@app.route('/index')
@requires_auth
def index():
  '''
  The Admin Panel
  '''
  return render_template('index.html') # static file from Vue build
