import re, json, os
from multiprocessing.pool import ThreadPool
from urllib import request
from util import helper

# ---- Edit
ENABLE_MULTITHREAD_DOWNLOADS = True
# ---- Edit

def get_query(string):
	m, d, y = helper.parse_date(string)
	return f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={y}-{m}-{d}&api_key=DEMO_KEY'

def get_urls(filepath):
	urls = []
	with open(filepath) as file:
		for line in file:
			query = get_query(line)
			print(query)

			with request.urlopen(query) as response:
				html = response.read()

			json_file = json.loads(html)
			
			for data in json_file['photos']:
				urls.append(data['img_src'])
	return urls

def download_images(url):
	target_path = os.path.join('./data', os.path.basename(url))
	request.urlretrieve(url, target_path)
	return f'Downloaded: {target_path}'

# create path if it doesn't exist
if not os.path.exists('./data'):
	os.mkdir('./data')

urls = get_urls('./input.txt')

if ENABLE_MULTITHREAD_DOWNLOADS:
	threads = ThreadPool(8).imap_unordered(download_images, urls)
	for thread in threads:
		print(thread)
else:
	for url in urls:
		download_images(url)