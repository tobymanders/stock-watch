# Displays all data in the SQLite database

import sqlite3

conn = sqlite3.connect('../data/database.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM instock'):
	print(row)

conn.close()