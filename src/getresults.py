# Displays all data in the SQLite database

import sqlite3
import json
import updatedb
import sys
import numpy as np
import mpu
import time

def get_timethresh(hours=24):
	return time.time() - hours*60*60

def main(address, product):


	input_lat, input_lng = updatedb.ziptolatlng(address)

	def dist(lat, long):
		coords_1 = (input_lat, input_lng)
		coords_2 = (lat, long)
		return mpu.haversine_distance(coords_1, coords_2) * 0.621371

	def format_time(seconds):
		if seconds < 60*60: #minutes case
			return f'{int(seconds/60)} minutes ago'
		elif seconds < 60*60*24: #hours case
			return f'{int(seconds/60/60)} hours ago'
		else:
			return f'{int(seconds/60/60/24)} days ago'

	def make_address(address, city, state):
		print(address)
		return ', '.join((str(address), city, state))


	conn = sqlite3.connect('../data/database.db')
	conn.create_function("dist", 2, dist)
	conn.create_function("format_time", 1, format_time)
	conn.create_function("make_address", 3, make_address)
	c = conn.cursor()


	productskus = {'AirPods' : 6084400, 'AirPods Pro' : 5706659}

	timethresh = get_timethresh(24*20)
	currtime = time.time()

	c.execute(f"""SELECT storename, retailer, make_address(address, city, state), city, state, ROUND(dist(lat, lng), 1), format_time({currtime} - time) 
				 FROM instock
				 WHERE dist(lat, lng) < 50 
				       AND sku={productskus[product]}
				       AND time>{timethresh}
				 GROUP BY storeID
				 ORDER BY dist(lat, lng) ASC""")



	data = c.fetchall()


	conn.close()
	return data

if __name__ == "__main__":
	if len(sys.argv) > 1:
		print(main(sys.argv[1]))
	else:
		print('Must provide an address.')