__author__ = 'Liew'

import sqlite3

conn = sqlite3.connect('fyp.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Log(
'l_id' INTEGER PRIMARY KEY AUTOINCREMENT, 'l_ip' TEXT, 'l_os' TEXT, 'l_port'	INTEGER, 'l_method' TEXT, 'l_atkduration' INTEGER, 'l_status' TEXT, 'l_solution' TEXT,
 'l_timestamp'	DATETIME DEFAULT CURRENT_TIMESTAMP)
''')

def findSolution(os):
    c.execute('SELECT s_website FROM Solutions WHERE s_os = ?', (os,))
    return c.fetchone()[0]

def getRecords():
    c.execute('SELECT * FROM Log')
    return c.fetchall()

def insertData(ip, os, port, method, time, status):
    c.execute('''INSERT INTO Log ('l_ip', 'l_os', 'l_port', 'l_method', 'l_atkduration', 'l_status', 'l_solution')
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (ip, os, int(port), method, int(time), status, findSolution(os)))
    conn.commit()




