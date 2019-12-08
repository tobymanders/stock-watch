# Displays all data in the SQLite database

import sqlite3
import json

def main():
	conn = sqlite3.connect('../data/database.db')
	c = conn.cursor()

	c.execute('SELECT * FROM instock')
	data = c.fetchall()

	return data

def return_locs():
	data = main()
	return [(item[-1], item[-2]) for item in data]


if __name__ == "__main__":
	res = main()
	for store in res:
		print(store[:8])
	print(f'{len(res)} RESULTS')
