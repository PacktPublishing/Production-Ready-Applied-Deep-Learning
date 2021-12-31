from bs4 import BeautifulSoup
import requests
from requests import get
import random
import sys
import traceback
import subprocess
# output file
f = open("./image_data/out_author_len.jpg", "w")


def extract_img_url(url):
    # http request
    response = get(url)
    # inside response, we have text field/parameter
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # print(response.text)
    # find all img tags and iterate
    for i in html_soup.select("img"):
        # get "src" attribute from the <img> tag
        link = i["src"]
        # author photo contains string view_photo, so match based on that
        if link.find("view_photo") >= 0:
            # print the link of image
            print(link)
            # write the image to output file
            f.write(requests.get(link).content)

            # cmd = ['wget', link]
            # subprocess.Popen(cmd)  # run the command to download
            # subprocess.Popen(cmd).communicate()


if __name__ == "__main__":
    csv_line = ""
    # seed url to start with
    url = 'https://scholar.google.com/citations?user=6JeebN0AAAAJ&hl=en'
    extract_img_url(url)