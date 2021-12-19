- This folder contains the py file to call rest API to collect JSON data.

- A copy of the locally stored JSON reddit file collected using REST API request
is located [here](./reddit.json)

- [get_rest_api_data.py](./get_rest_api_data.py) is used to make python library `urllib` request object `request` to
REST endpoint [here](https://www.reddit.com/r/all.json) that returns JSON file. The JSON
data is then saved as JSON object using `json.loads()` from `json` library and then
the parsed further. The parsed elements such as author_fullname, selftext,  is_video, title, upvote_ratio, 
is_original_content, media_embed are saved into the CSV file [reddit.csv](./reddit.csv)

- Notes for [get_rest_api_data.py](./get_rest_api_data.py)

     -  is_read_local_json - if set True, read from locally stored json file. if False, call REST JSON endpoint to get data