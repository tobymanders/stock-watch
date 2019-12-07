# Displays all data in the SQLite database

import sqlite3
import json

def main(zip_code):
	conn = sqlite3.connect('../data/database.db')
	c = conn.cursor()

	c.execute('SELECT * FROM instock LIMIT 1')
	data = c.fetchall()
	return data

if __name__ == "__main__":
	print(main())