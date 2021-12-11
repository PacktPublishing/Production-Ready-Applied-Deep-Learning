# This script collects the API data from Reddit
import requests

# URL that needs to be crawled for JSON object. Should return jSON
url = 'https://www.reddit.com/r/all.json'

# reques object. If you get "Too Many requests" error, try after 1-2 minutes
resp = requests.get(url=url)

# Json object
json_data = resp.json()

print(json_data)

# The json structure has the actual data inside "data" -> "children"
json_children = json_data["data"]["children"]

# iterate each children data
for i in json_children:
    author = i["author_fullname"]
    text = i["selftext"]
    category = i["category"]
    title = i["title"]
    upvote_ratio = i["upvote_ratio"]
    is_original = i["is_original_content"]
    media_embed = i["media_embed"]