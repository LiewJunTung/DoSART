# CREATE TABLE `Solutions` (
# `s_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
# `s_os`	TEXT REFERENCES OperatingSystem(os_id) ON UPDATE CASCADE,
# `s_atk`	TEXT REFERENCES AttackMethod(atk_id) ON UPDATE CASCADE,
# `s_solution`	TEXT
# );

__author__ = 'Liew'

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/fyp.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
    app.run()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    #cur = g.db.execute('select title, text from entries order by id desc')
    cur0 = g.db.execute('select os_id, os_name from OperatingSystem order by os_id desc')
    entries0 = [dict(os_id=row[0], os_name=row[1]) for row in cur0.fetchall()]
    cur1 = g.db.execute('select atk_id, atk_name from AttackingMethod order by atk_id desc')
    entries1 = [dict(atk_id=row[0], atk_name=row[1]) for row in cur1.fetchall()]
    #
    # for x in entries0:
    #     for y in entries1:


    # cur2 = g.db.execute('select s_solution from Solutions where s_os = ? and s_atk = ?', (x0, x1))

    cur = g.db.execute('select e_sol, e_text from entries where e_sol=?', )
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)