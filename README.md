# image_fetch
- Fetches images from specific dates from images of NASA using their API.

## Running
- Run via command `python image_fetch.y`
- You can change the dates in the `input.txt` file to fetch images in those dates.

## API KEY
- This uses the 'NASA_API' api key by default. If it doesn't find it, it sets to 'DEMO_KEY' which is given by NASA. It is only limited to a number of calls.
- If you need your own API key, you can get one from [here](https://api.nasa.gov/) and set it as an environment variable under the key 'API_KEY'.

## Requirements
- Python 3