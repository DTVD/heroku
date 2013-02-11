# import
from __future__ import with_statement
from contextlib import closing
import sqlite3,os
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

# config
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'DTVD'
PASSWORD = 'google'

# create
app = Flask(__name__)
app.config.from_object(__name__)

# db
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

# view
@app.route('/')
def show_users():
    if not session.get('logged_in'):
        users = []
    else:
        cur = g.db.execute('select name, age from users order by id desc')
        users = [dict(name=row[0], age=row[1]) for row in cur.fetchall()]
    return render_template('users.html', entries=users)

# add an user info
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into users (name, age) values (?, ?)',
                 [request.form['name'], request.form['age']])
    g.db.commit()
    flash('New user was successfully added')
    return redirect(url_for('show_users'))

# del an user info
@app.route('/del', methods=['POST'])
def del_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('delete from users where name= ? ',
                 [request.form['name']])
    g.db.commit()
    flash('user successfully deleted')
    return redirect(url_for('show_users'))

# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_users'))
    return render_template('login.html', error=error)

# logout 
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_users'))

# hello flaskr
@app.route('/hello')
def hello():
    return """
    contact me at vunhatminh@icloud.com 
    """

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
