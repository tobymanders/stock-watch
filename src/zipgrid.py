import numpy as np
import geocoder as gc
import pickle as pkl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

nwcorner = (48.717487, -124.525622)
secorner = (25.242196, -67.866524)


num_vert = 15
num_horiz = 22

lats = np.linspace(nwcorner[0], secorner[0], num_vert)
lngs = np.linspace(nwcorner[1], secorner[1], num_horiz)

def get_latlng_grid(lats=lats, lngs=lngs):
	return [(lat, lng) for lat in lats for lng in lngs]
		

def get_zips(lats=lats, lngs=lngs):
	latlng_grid = get_latlng_grid(lats, lngs)
	gc_api_key = '9GOLlJifpGuxjGPy2519C6NkcmtXxAYM'
	
	gs = []
	postals = []
	nopostals = []
	for latlng in latlng_grid:
		print(latlng)
		g = gc.mapquest(latlng, key=gc_api_key, method='reverse')
		gs.append(g)
		if g.postal:
			postals.append(latlng)
			print('POSTAL!')
		else:
			nopostals.append(latlng)
			print('NO POSTAL!', g.status_code)
		time.sleep(0.1)

	print(len(gs))
	
	return {res.postal[:5] for res in gs if res.postal[:5].isnumeric()}, postals, nopostals
	# return g.postal

def plot_postals(postals, nopostals):
	plt.scatter([i[1] for i in postals], [i[0] for i in postals], c='blue')
	plt.scatter([i[1] for i in nopostals], [i[0] for i in nopostals], c='red')
	img = mpimg.imread('../data/map.png')
	map_extent = [-128.322621, -65.408390, 23.679990, 50.749919]
	plt.imshow(img, extent=map_extent, alpha=1) # The coordinates of my Google Maps screenshot.
	plt.gca().set_aspect('equal')
	plt.show()

if __name__ == '__main__':
	zips, postals, nopostals = get_zips(lats, lngs)
	pkl.dump((list(zips), postals, nopostals), open('../data/zips.pkl', 'wb'))
	print(zips)
	print(len(zips))
	plot_postals(postals, nopostals)