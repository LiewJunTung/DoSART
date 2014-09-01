__author__ = 'Liew'

import sqlite3

conn = sqlite3.connect('fyp.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Log(
l_id INTEGER PRIMARY KEY AUTOINCREMENT,
l_ip TEXT,
l_os INTEGER REFERENCES OperatingSystem(os_id),
l_port INTEGER,
l_method INTEGER REFERENCES attackMethod(atk_id),
l_atkduration INTEGER,
l_sensitivity INTEGER,
l_maxpacket INTEGER,
l_fixapplied TEXT,
l_result TEXT,
l_img	TEXT,
l_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);
''')

def findSolution(os):
    c.execute('SELECT s_website FROM Solutions WHERE s_os = ?', (os,))
    return c.fetchone()[0]

def getRecords():
    c.execute('SELECT * FROM Log')
    return c.fetchall()

def getimage():
    c.execute('SELECT l_img FROM Log WHERE l_id = 3')
    return c.fetchone()

def insertData(ip, os, port, method, atkduration, sensitivity, maxpacket, fixapplied, result, img):
    c.execute('''
INSERT INTO Log ('l_ip', 'l_os', 'l_port', 'l_method', 'l_atkduration', 'l_sensitivity',
 'l_maxpacket', 'l_fixapplied', 'l_result', 'l_img')
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ip, os, int(port), method, int(atkduration),
          float(sensitivity), maxpacket, fixapplied, result, img))
    conn.commit()




