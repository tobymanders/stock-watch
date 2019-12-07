## Script to update the SQL database with fresh data. 
## This should be run on regular cadence.


import requests
import time
import sqlite3
import geocoder as gc

def ziptolatlng(address):
	api_key = '9GOLlJifpGuxjGPy2519C6NkcmtXxAYM'
	g = gc.mapquest(address, key=api_key)
	if g.status_code==200:
		lat, lng = g.latlng
	else:
		lat, lng = 500, 500
	return lat, lng


def update_bestbuy():
	# Set up Best Buy requests
	bb_api_key = 'Syg9LF6J4rNlfmYpxgzCejev'
	bb_product_skus = {'airpods':'6084400'}
	zip_codes = ['55423', '44121']
	bb_base_url = "https://api.bestbuy.com/v1/products/product_sku/stores.json?postalCode=zip_code&apiKey=" + bb_api_key

	# Make requests and parse results
	new_results = []
	for product, sku in bb_product_skus.items():
		for zip_code in zip_codes:
			request_url = bb_base_url.replace('product_sku', sku).replace(
				'zip_code', zip_code)

			print(request_url)

			req_time = time.time()

			res = requests.get(request_url)

			if res.status_code == 200:
				json = res.json()


				info = [(req_time, item['storeID'], item['name'], item['address'], item['city'],
					item['state'], item['postalCode'], product, sku,
						*ziptolatlng(item['address'] + item['city'] + item['state'] + item['postalCode']))
						for item in json['stores']]

				new_results.extend(info)

			time.sleep(0.5)



	# Connect to and update database
	conn = sqlite3.connect('../data/database.db')
	c = conn.cursor()
	c.executemany('INSERT INTO instock VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', new_results)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	update_bestbuy()