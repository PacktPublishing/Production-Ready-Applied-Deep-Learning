# This script collects the API data from Reddit
import json
import re
import traceback
import urllib.request as request
import pandas as pd

# if set True, read from locally stored json file. if False, call REST JSON endpoint to get data
is_read_local_json = True


def json_to_csv(url, in_file, out_file):
    try:
        # file for output csv
        f_out = open(out_file, "w")
        # header for output CSV
        header_out_csv = "author_fullname,text,is_video,title,is_original_content,media_embed"
        f_out.write(header_out_csv + '\n')
        # read from locally stored JSON file
        if is_read_local_json:
            print("Read from locally saved JSON file")
            # open JSON file for reading
            f = open(in_file, "r")
            json_data = json.load(f)
        else:
            print("Read from REST endpoint of Reddit")
            # json request to get response
            response = request.urlopen(url)
            # read the response
            source = response.read()
            # json loads to save as a JSON object for further parsing
            json_data = json.loads(source)
        # In the JSON, retrieve the list of "children" objects inside "data" object.
        data_children = json_data["data"]["children"]
        # iterate each children data
        for i in data_children:
            # Read "data" object inside each "children" object, which has the attributes such as author_fullname,
            #  selftext,  is_video, title, upvote_ratio, is_original_content, media_embed
            data_obj = i["data"]
            # print(i)
            author = remove_comma(data_obj["author_fullname"])
            # feature "selftext" -> text data. Needs a set of processing such as remove comma, remove
            # non-alphanumeric characters, convert to lower case
            text = remove_comma(data_obj["selftext"])
            # replace new line in the text file. Otherwise the line will split into multiple in the output CSV file.
            text = text.replace("\n", "")
            # remove non alpha-numeric characters
            text = clean_text(text)
            # convert string to lower case
            text = convert_lowercase(text)
            # "title" -> needs set of cleaning similar to one did for the feature "text"
            title = remove_comma(data_obj["title"])
            # remove non alpha-numeric characters
            title = clean_text(title)
            # convert string to lower case
            title = convert_lowercase(title)
            is_video = remove_comma(data_obj["is_video"])
            upvote_ratio = remove_comma(data_obj["upvote_ratio"])
            is_original = remove_comma(data_obj["is_original_content"])
            media_embed = remove_comma(data_obj["media_embed"])
            # concatenate all extracted features into a single line for writing
            curr_line = f"{author},{text},{is_video},{title},{upvote_ratio},{is_original},{media_embed}"
            f_out.write(str(curr_line) + "\n")
        print("END...")
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


def convert_lowercase(in_str):
    """ Convert a given string to lower case
    :param in_str:
    :return:
    """
    return str(in_str).lower()

def is_empty()

if __name__ == "__main__":
    # URL that needs to be crawled for JSON data object. Should return jSON
    url = 'https://www.reddit.com/r/all.json'
    # if the read from REST endpoint for JSON fails due to too many tries, read from already saved JSON file below
    in_file = "./reddit.json"
    # output file
    out_file = "./reddit.csv"
    # collect Reddit JSON data and save as csv
    json_to_csv(url, in_file, out_file)

############################################################################################################
# NOTES:
############################################################################################################
# Text before and after realing with regex library "re"
# BEFORE -> As the title says I dispatch for 911. Last night I got a call for a domestic disturbance. The woman calling was so scared. She kept saying "he's gonna kill me he's gonna fucking kill me". I went through my protocol and tried to keep her calm. Dispatchers have a system called ProQA that gives guidance on what to do in certain situations. I followed that and had the police and Ambulance en route as soon as possible. I tried to tell her to get to a safe place and kept assuring her help was on the way. She said she had locked herself in the bathroom. I could hear him pounding on the door yelling "you're dead. I'm gonna fucking kill you". I did everything I could. I tried to keep her calm and help her but she was trapped. I told her I was here for her and she wasn't alone. She told me about her child a 4 year old girl and that she wasn't going to leave her. Time seemed to drag on. I checked with my officers who were only 2 minutes out and I felt some relief. I just knew she was going to be okay. Until I heard the sound of the door being kicked down. All she said was "God help me" and the most haunting scream I have ever heard and dropped the phone. 3 shots followed and I never heard from her again. My crews arrived on scene and the husband was detained. She was dead. One shot to the head two to the chest. I cannot stop replaying our conversation. I can't get her fear and screams out of my head. I knew what I was getting into when I took this job I just feel so helpless and sad. I have an appointment with our work grief counseling Monday. Anyways thanks for listening. Just needed to tell someone.,False,I'm a 911 dispatcher. Last night I heard a murder and I feel really messed up.
# AFTER  -> As the title says I dispatch for 911 Last night I got a call for a domestic disturbance The woman calling was so scared She kept saying he s gonna kill me he s gonna fucking kill me I went through my protocol and tried to keep her calm Dispatchers have a system called ProQA that gives guidance on what to do in certain situations I followed that and had the police and Ambulance en route as soon as possible I tried to tell her to get to a safe place and kept assuring her help was on the way She said she had locked herself in the bathroom I could hear him pounding on the door yelling you re dead I m gonna fucking kill you I did everything I could I tried to keep her calm and help her but she was trapped I told her I was here for her and she wasn t alone She told me about her child a 4 year old girl and that she wasn t going to leave her Time seemed to drag on I checked with my officers who were only 2 minutes out and I felt some relief I just knew she was going to be okay Until I heard the sound of the door being kicked down All she said was God help me and the most haunting scream I have ever heard and dropped the phone 3 shots followed and I never heard from her again My crews arrived on scene and the husband was detained She was dead One shot to the head two to the chest I cannot stop replaying our conversation I can t get her fear and screams out of my head I knew what I was getting into when I took this job I just feel so helpless and sad I have an appointment with our work grief counseling Monday Anyways thanks for listening Just needed to tell someone ,False,I'm a 911 dispatcher. Last night I heard a murder and I feel really messed up.
