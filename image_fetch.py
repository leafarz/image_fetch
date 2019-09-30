import re, json, os
from multiprocessing.pool import ThreadPool
from urllib import request
from util import helper

# ---- Edit
ENABLE_MULTITHREAD_DOWNLOADS = True

# TODO: move to config
API_KEY = os.environ.get('NASA_API', 'DEMO_KEY')
# ---- Edit

# Functions
def get_query_data(string):
	m, d, y = helper.parse_date(string)

	return (
		y + m + d,
		f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={y}-{m}-{d}&api_key=' + API_KEY
	)

def get_url_data(filepath):
	url_data = []
	with open(filepath) as file:
		for line in file:
			date, api = get_query_data(line)
			print(f'Getting api from: {api}')

			with request.urlopen(api) as response:
				html = response.read()

			json_file = json.loads(html)

			# create folder to put the photos
			if not os.path.exists('./data/' + date):
				os.mkdir('./data/' + date)

			# set the data
			for data in json_file['photos']:
				url_data.append({
					"date": date,
					"url": data["img_src"]
				})
	return url_data

def download_images(url_data):
	target_path = os.path.join('./data/' + url_data['date'], os.path.basename(url_data['url']))
	request.urlretrieve(url_data['url'], target_path)
	return f'Downloaded: {target_path}'
# Functions

if __name__ == '__main__':
	# create path if it doesn't exist
	if not os.path.exists('./data'):
		os.mkdir('./data')

	url_data = get_url_data('./input.txt')

	if ENABLE_MULTITHREAD_DOWNLOADS:
		threads = ThreadPool(8).imap_unordered(download_images, url_data)
		for thread in threads:
			print(thread)
	else:
		for data in url_data:
			download_images(data)