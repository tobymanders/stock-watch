## Script to update the SQL database with fresh data. 
## This should be run on regular cadence.
## Must have database and latlng pickle files already in place.


import requests
import time
import sqlite3
import geocoder as gc
import pickle

nzips = 200 # take top n zip codes by population
zips = pickle.load(open('../data/zips.pkl', 'rb'))[:nzips]

gc_api_key = '9GOLlJifpGuxjGPy2519C6NkcmtXxAYM'
latlngdict = pickle.load(open('../data/latlngdict.pkl', 'rb'))

def ziptolatlng(address):

	if address in latlngdict:
		lat, lng = latlngdict[address]
	else:
		g = gc.mapquest(address, key=gc_api_key)
		if g.status_code==200:
			lat, lng = g.latlng
			latlngdict[address] = (lat, lng) # Store so do not have to fetch next time
			pickle.dump(latlngdict, open('../data/latlngdict.pkl', 'wb'))
		else:
			lat, lng = 500, 500
	return lat, lng

def extract_data(json, product, sku):

	req_time = time.time()

	info = [(req_time, item['storeID'], item['name'], item['address'], 'Best Buy', item['city'],
			item['state'], item['postalCode'], product, sku,
			*ziptolatlng(item['address'] + ' ' + item['city'] + ' ' +  item['state'] + ' ' + item['postalCode'])) for item in json['stores']]

	return info


def request_json(url, zip_code):

	print(f'REQUESTING ZIP CODE {zip_code}...')

	res = requests.get(url)

	if res.status_code==200:
		return res.json()
	else:
		print('REQUEST FAILED')
		return None


def add_results_to_db(new_results):
	# Connect to and update database
	conn = sqlite3.connect('../data/database.db')
	c = conn.cursor()
	c.executemany('INSERT INTO instock VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', new_results)
	conn.commit()
	conn.close()
	print(f'SUCCESSFULLY ADDED {len(new_results)} records to the database')



def update_bestbuy():
	# Set up Best Buy requests
	bb_api_key = 'Syg9LF6J4rNlfmYpxgzCejev'
	bb_product_skus = {'airpods_pro': '5706659', 'airpods': '6084400'}
	zip_codes = [str(zip_) for zip_ in zips]
	bb_base_url = 'https://api.bestbuy.com/v1/products/'
	attribs = "?postalCode="

	new_results = []
	for product, sku in bb_product_skus.items():
		for zip_code in zip_codes:


			request_url = bb_base_url + sku + '/stores.json' + attribs + zip_code + '&apiKey=' + bb_api_key
			json = request_json(request_url, zip_code)

			if json:
				stores = extract_data(json, product, sku)
				new_results.extend(stores)
				print(f'FOUND {len(stores)} STORES')

		add_results_to_db(new_results)



if __name__ == '__main__':
	update_bestbuy()