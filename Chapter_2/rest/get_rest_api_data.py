# This script collects the API data from Reddit
import requests
import urllib.request as request
import traceback
import json


def json_to_csv(url, out_file):
    try:
        # file for output csv
        f = open(out_file, "w")
        # request object. If you get "Too Many requests" error, try after 5 minutes
        # resp = requests.get(url=url)
        # print(type(resp))
        # # Json object
        # json_data = resp.json()
        # print(type(json_data))
        # print(json_data)
        # # The json structure has the actual data inside "data" -> "children"
        # # json_children = json_data["data"]["children"]
        # json_data = json.load(resp)

        response = request.urlopen(url)
        source = response.read()
        json_data = json.loads(source)
        type(json_data)
        json_data.keys()
        type(json_data['data'])
        json_data['data'].keys()
        json_children = json_data['data']['children']
        print(json_children)
        print("======")
        # iterate each children data
        for i in json_children:
            print(i)
            author = remove_comma(i["author_fullname"])
            text = remove_comma(i["selftext"])
            category = remove_comma(i["category"])
            title = remove_comma(i["title"])
            upvote_ratio = remove_comma(i["upvote_ratio"])
            is_original = remove_comma(i["is_original_content"])
            media_embed = remove_comma(i["media_embed"])
            # concatenate all features
            curr_line = f"{author},{text},{category},{title},{upvote_ratio},{is_original},{media_embed}"
            f.write(curr_line + "\n")

        f.close()
    except Exception:
        traceback.print_exc()


def remove_comma(in_str):
    """ Remove comma from given string
    """
    return in_str.replace(",", " ").replace("  ", " ")


if __name__ == "__main__":
    # URL that needs to be crawled for JSON object. Should return jSON
    url = 'https://www.reddit.com/r/all.json'
    # output file
    out_file = "./reddit.csv"
    # collect reddit JSON data and save as csv
    json_to_csv(url, out_file)
