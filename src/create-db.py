# NOTE: MUST CREATE database.db BEFORE RUNNING: 
#!sqlite3 
#!.open ../data/database.db

import sqlite3

conn = sqlite3.connect('../data/database.db')

c = conn.cursor()

c.execute('DROP TABLE instock')

c.execute('''CREATE TABLE instock
			 (time real, storeID text, storename text, address text, retailer text,
			 city text, state text, zipcode text, product text, sku int, lat real, lng real)''')

conn.commit()

conn.close()