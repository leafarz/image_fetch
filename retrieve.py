import re, json, os
from urllib import request
from util import helper

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

def download_images(urls):
	for url in urls:
		target_path = os.path.join('./data', os.path.basename(url))
		request.urlretrieve(url, target_path)
		print(f'Downloaded: {target_path}')

# create path if it doesn't exist
if not os.path.exists('./data'):
	os.mkdir('./data')

urls = get_urls('./input.txt')
download_images(urls)