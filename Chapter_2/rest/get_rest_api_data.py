# This script collects the API data from Reddit
import requests
import urllib.request as request
import traceback
import pandas as pd
import re
import json

# if set True, read from locally stored json file. if False, call REST JSON endpoint to get data
is_read_local_json = True


def json_to_csv(url, out_file):
    try:
        # file for output csv
        f_out = open(out_file, "w")
        # header for output CSV
        header_out_csv = "author_fullname,selftext,is_video,title,is_original_content,media_embed"
        f_out.write(header_out_csv + '\n')
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

        if is_read_local_json:
            print("Read from locally saved JSON file")
            # read from locally stored JSON file
            # Opening JSON file
            f = open("./reddit.json", "r")
            json_data = json.load(f)
        else:
            print("Read from REST endpoint of Reddit")
            response = request.urlopen(url)
            source = response.read()
            json_data = json.loads(source)

        data_children = json_data["data"]["children"]
        # print("data_children")
        print(data_children)
        # json_children = json_data['data']['children']
        # print(json_children)
        print("======")

        # iterate each children data
        for i in data_children:
            data_obj = i["data"]
            # print(i)
            author = remove_comma(data_obj["author_fullname"])
            # print(author)
            text = remove_comma(data_obj["selftext"])
            # replace new line in the text file. Otherwise the line will split into multiple in the output CSV file.
            text = text.replace("\n", "")
            # remove non alpha-numeric characters
            text = clean_text(text)
            is_video = remove_comma(data_obj["is_video"])
            title = remove_comma(data_obj["title"])
            upvote_ratio = remove_comma(data_obj["upvote_ratio"])
            is_original = remove_comma(data_obj["is_original_content"])
            media_embed = remove_comma(data_obj["media_embed"])
            # concatenate all features
            curr_line = f"{author},{text},{is_video},{title},{upvote_ratio},{is_original},{media_embed}"
            print(curr_line)
            f_out.write(str(curr_line) + "\n")

        f_out.close()
    except Exception:
        traceback.print_exc()


def remove_comma(in_str):
    """ Remove comma from given string
    """
    return str(in_str).replace(",", " ").replace("  ", " ")


def clean_text(in_str):
    """ Remove unwanted characters like ", [, ], ?
    :param in_str:
    :return:
    """
    clean_txt = re.sub(r'\W+', ' ', in_str)
    return clean_txt

if __name__ == "__main__":
    # URL that needs to be crawled for JSON object. Should return jSON
    url = 'https://www.reddit.com/r/all.json'
    # output file
    out_file = "./reddit.csv"
    # collect Reddit JSON data and save as csv
    json_to_csv(url, out_file)



# Text before and after realing with regex library "re"
# BEFORE -> As the title says I dispatch for 911. Last night I got a call for a domestic disturbance. The woman calling was so scared. She kept saying "he's gonna kill me he's gonna fucking kill me". I went through my protocol and tried to keep her calm. Dispatchers have a system called ProQA that gives guidance on what to do in certain situations. I followed that and had the police and Ambulance en route as soon as possible. I tried to tell her to get to a safe place and kept assuring her help was on the way. She said she had locked herself in the bathroom. I could hear him pounding on the door yelling "you're dead. I'm gonna fucking kill you". I did everything I could. I tried to keep her calm and help her but she was trapped. I told her I was here for her and she wasn't alone. She told me about her child a 4 year old girl and that she wasn't going to leave her. Time seemed to drag on. I checked with my officers who were only 2 minutes out and I felt some relief. I just knew she was going to be okay. Until I heard the sound of the door being kicked down. All she said was "God help me" and the most haunting scream I have ever heard and dropped the phone. 3 shots followed and I never heard from her again. My crews arrived on scene and the husband was detained. She was dead. One shot to the head two to the chest. I cannot stop replaying our conversation. I can't get her fear and screams out of my head. I knew what I was getting into when I took this job I just feel so helpless and sad. I have an appointment with our work grief counseling Monday. Anyways thanks for listening. Just needed to tell someone.,False,I'm a 911 dispatcher. Last night I heard a murder and I feel really messed up.
# AFTER  -> As the title says I dispatch for 911 Last night I got a call for a domestic disturbance The woman calling was so scared She kept saying he s gonna kill me he s gonna fucking kill me I went through my protocol and tried to keep her calm Dispatchers have a system called ProQA that gives guidance on what to do in certain situations I followed that and had the police and Ambulance en route as soon as possible I tried to tell her to get to a safe place and kept assuring her help was on the way She said she had locked herself in the bathroom I could hear him pounding on the door yelling you re dead I m gonna fucking kill you I did everything I could I tried to keep her calm and help her but she was trapped I told her I was here for her and she wasn t alone She told me about her child a 4 year old girl and that she wasn t going to leave her Time seemed to drag on I checked with my officers who were only 2 minutes out and I felt some relief I just knew she was going to be okay Until I heard the sound of the door being kicked down All she said was God help me and the most haunting scream I have ever heard and dropped the phone 3 shots followed and I never heard from her again My crews arrived on scene and the husband was detained She was dead One shot to the head two to the chest I cannot stop replaying our conversation I can t get her fear and screams out of my head I knew what I was getting into when I took this job I just feel so helpless and sad I have an appointment with our work grief counseling Monday Anyways thanks for listening Just needed to tell someone ,False,I'm a 911 dispatcher. Last night I heard a murder and I feel really messed up.
