from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.users.models import User
from app.users.decorators import requires_login

def before_request():
  """
  pull user's profile from the database before every request are treated
  """
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id']);


