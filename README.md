# image_fetch
- Fetches images from specific dates from images of NASA using their API.
- Can be viewed in browser.

## Running
- Run via command `python image_fetch.py` and it will download files via dates in `input.txt` file.
- This will open the browser upon finishing download. If for some reason a text editor is opened,
this is probaby because that editor is set as default for opening html files. Just open the
`index.html` under the *static* folder via browser. (There is no hosting involved, just all static files)
- You can change the dates in the `input.txt` file to fetch images in those dates.

## API KEY
- This uses the 'NASA_API' api key. If it doesn't find it, it sets to 'DEMO_KEY' by default. This demo api key is given by NASA and it is only limited to a number of calls.
- If you need your own API key, you can get one from [here](https://api.nasa.gov/) and set it as an environment variable under the key 'API_KEY'.

## Requirements
- Python 3