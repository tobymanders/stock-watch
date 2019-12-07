# NOTE: MUST CREATE database.db BEFORE RUNNING: 
#!sqlite3 
#!.open ../data/database.db

import sqlite3

conn = sqlite3.connect('../data/database.db')

c = conn.cursor()

c.execute('''CREATE TABLE instock
			 (time real, storeID text, storename text, address text,
			 city text, state text, zipcode text, product text, sku text, lat real, long real)''')

conn.commit()

conn.close()