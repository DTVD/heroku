from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.twitter.forms import RegisterForm
from app.users.models import User
from app.twitter.models import Twitter 
from app.users.decorators import requires_login
import tweepy
from app.twitter import constants as CONSTANTS 

mod = Blueprint('twitter', __name__, url_prefix='/twitter')

@requires_login
@mod.route('/register/', methods=['GET', 'POST'])
def register():
  """
  Twitter Registration 
  """

  auth = tweepy.OAuthHandler(CONSTANTS.CONSUMER_KEY, CONSTANTS.CONSUMER_SECRET)
  auth_url = auth.get_authorization_url()

  form = RegisterForm(request.form)
  if form.validate_on_submit():
    twitter = Twitter(form.twitter_id.data, session['user_id'])
    db.session.add(twitter)
    db.session.commit()

    flash('Thanks for adding twitter account')
    return redirect(url_for('users.home'))

  t = Twitter.query.filter_by(uid=g.user.id)
  return render_template("twitter/register.html", form=form, twitter = t, oauth = auth_url)
