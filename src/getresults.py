# Displays all data in the SQLite database

import sqlite3
import json
import updatedb
import sys
import numpy as np
import mpu

def main(address, product):


	input_lat, input_lng = updatedb.ziptolatlng(address)

	def dist(lat, long):
		coords_1 = (input_lat, input_lng)
		coords_2 = (lat, long)
		return mpu.haversine_distance(coords_1, coords_2) * 0.621371


	conn = sqlite3.connect('../data/database.db')
	conn.create_function("dist", 2, dist)
	c = conn.cursor()


	productskus = {'AirPods' : 6084400, 'AirPods Pro' : 5706659}

	c.execute(f"""SELECT storename, retailer, address, city, state, ROUND(dist(lat, lng), 1)
				 FROM instock
				 WHERE dist(lat, lng) < 50 AND sku={productskus[product]}
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