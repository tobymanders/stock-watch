# Displays all data in the SQLite database

import sqlite3
import json
import updatedb
import sys
import numpy as np
import mpu

def main(address):


	input_lat, input_lng = updatedb.ziptolatlng(address)

	def dist(lat, long):
		# return geopy.distance.distance((input_lat, input_lng), (lat, long))
		coords_1 = (input_lat, input_lng)
		coords_2 = (lat, long)
		return mpu.haversine_distance(coords_1, coords_2)


	conn = sqlite3.connect('../data/database.db')
	conn.create_function("dist", 2, dist)
	c = conn.cursor()





	# c.execute('''SELECT city, state, address, zipcode FROM instock
	# 		     LIMIT 5''')
	# data = c.fetchall()


	# c.execute(f'''
	# SELECT city, state, address, zipcode, (6371 * acos( cos( radians({input_lat}) ) * cos( radians( lat ) ) * cos( radians( {input_lng} ) - radians(long) ) + sin( radians({input_lat}) ) * sin( radians(coord_lat) ) )) AS distanta
	# FROM instock
	# WHERE lat<>''
	# 	AND long<>''
	# HAVING distanta<50
	# ORDER BY distanta desc''')

	c.execute('''SELECT storename, dist(lat, long)
				 FROM instock
				 WHERE dist(lat, long) < 100''')



	data = c.fetchall()


	conn.close()
	return data

if __name__ == "__main__":
	if len(sys.argv) > 1:
		print(main(sys.argv[1]))
	else:
		print('Must provide an address.')