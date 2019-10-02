# image_fetch
- Fetches images from specific dates from images of NASA using their API.
- Can be viewed in browser.

## Running
- Run via command `python image_fetch.py` and it will download files via dates in `input.txt` file.
- This will open the browser upon finishing download. If for some reason a text editor is opened,
this is probaby because that editor is set as default for opening html files. Just open the
`index.html` under the *static* folder via browser. (There is no hosting involved, just all static files)
- You can change the dates in the `input.txt` file to fetch images in those dates.

## Configuration
- API Key
  - `NASA_API`: This is your API key that must be set in your environment variables.
  - `DEMO_KEY`: This is the API key used by the script if `NASA_API` is not found. This is the demo api key given by NASA and it is only limited to a number of calls.
  - If you need your own API key, you can get one from [here](https://api.nasa.gov/) and set it as an environment variable under the key 'API_KEY'.
- Multithread download
  - This is set via `ENABLE_MULTITHREAD_DOWNLOADS` in the `image_fetch.py` script
  - Currently it's set to `True` and can be toggled to `False` if preferred (or for some reason there are issues with multithreading).

## Scripts
- `image_fetch.py`: the main script to run image fetching and viewing via browser.
- `test_dates.py`: script to test different cases of input dates

## Requirements
- Python 3