from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.facebook.forms import RegisterForm
from app.users.models import User
from app.facebook.models import Facebook 
from app.users.decorators import requires_login

mod = Blueprint('facebook', __name__, url_prefix='/facebook')

@mod.before_request
def before_request():
  """
  pull user's profile from the database before every request are treated
  """
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id']);
    g.facebook = Facebook.query.filter_by(uid=session['user_id']).first()

@requires_login
@mod.route('/register/', methods=['GET', 'POST'])
def register():
  """
  Facebook Registration 
  """
  form = RegisterForm(request.form)
  if form.validate_on_submit():
    facebook = Facebook(form.facebook_id.data, session['user_id'])
    db.session.add(facebook)
    db.session.commit()

    flash('Thanks for adding facebook account')
    return redirect(url_for('users.home'))
  return render_template("facebook/register.html", form=form, facebook = g.facebook)
