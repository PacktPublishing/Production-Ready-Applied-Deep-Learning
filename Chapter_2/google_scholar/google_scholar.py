# Collect Google Scholar authors html pages from web and convert to CSV
from bs4 import BeautifulSoup
from requests import get
import random
import sys
import traceback
import csv

# debug flag
is_debug = False
# max authors to be crawled
LIMIT_MAX_AUTHORS = 10000
# keeps record of all crawled url so far
lst_already_crawled_url = []
# holds all the urls collected from co-author list to be crawled further
lst_global_url = []
# output file
filename = "output.csv"


def write_to_file(filename, str_line, count):
    if count == 1:
        mode = 'w'
        header = "author_name,email,affiliation,coauthors_names,research_interest"
    else:
        mode = 'a'
    # writing to csv file
    with open(filename, mode) as csvfile:
        if count == 1:
            csvfile.write(header + "\n")
        csvfile.write(str_line + "\n")


def crawl_author(url):
    # Research Interest
    lst_resear_int = []
    lst_coauthors_link = []
    lst_coauthor_name = []
    # concatenated strings
    resear_int_conc = ""
    coauthors_link_conc = ""
    coauthor_name_conc = ""
    univ_new = ""

    # http request
    response = get(url)
    # inside response, we have text field/parameter
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # print(html_soup.prettify())

    # For loop to iterate each of the href attribute value found inside <a> tag
    for a in html_soup.find_all('a', href=True):

        # print("Found the URL (ALL):", a['href'])

        # research interest
        temp1 = str(a).find("mauthors=label:")  # .find is used to do "substring finding"..
        if temp1 >= 0:
            if is_debug:
                print("RI: Found the URL:", a['href'])
            ri = str(a['href']).replace("/citations?view_op=search_authors&hl=en&oe=ASCII&mauthors=label:", "")
            lst_resear_int.append(ri)
            if len(resear_int_conc) == 0:
                resear_int_conc = ri
            else:
                resear_int_conc = resear_int_conc + "##" + ri# use ## as delimiter
            if is_debug:
                print("temp1: " + str(temp1) + " current url:" + a['href'])

        # co-author related links
        temp2 = str(a).find("/citations?user=")  # .find is used to do "substring finding"..
        if temp2 >= 0:
            if is_debug:
                print("Co-Author: Found the URL:", a['href'])
            ca = "https://scholar.google.com" + str(a['href'])
            lst_coauthors_link.append(ca)
            lst_global_url.append(ca)
            if len(coauthors_link_conc) == 0:
                coauthors_link_conc = ca
            else:
                coauthors_link_conc = coauthors_link_conc + "##" + ca  # use ## as delimiter
            if is_debug:
                print("temp2: " + str(temp2) + " current url:" + a['href'])
            # Get name of co-author
            temp3 = str(a).find(">", temp2) + 1
            temp4 = str(a).find("<", temp3)
            coauthor_name = str(a)[temp3: temp4]
            if len(coauthor_name_conc) == 0:
                coauthor_name_conc = coauthor_name
            else:
                coauthor_name_conc = coauthor_name_conc + "##" + coauthor_name  # use ## as delimiter
            lst_coauthor_name.append(coauthor_name)

    print("-------------")
    print("list research interests:" + str(lst_resear_int))
    print("list co-authors link:" + str(lst_coauthors_link))
    print("list co-authors names:" + str(lst_coauthor_name))

    # Name
    main_author_name = html_soup.select('div#gsc_prf_in')[0].get_text()
    print(main_author_name)

    # Get official email id
    main_email = html_soup.select('div#gsc_prf_ivh')[0].get_text()
    main_email = main_email.replace("Verified email at ", "").replace(" - Homepage", "")
    print(main_email)

    # University / affiliation
    # univ = html_soup.find_all('href', class_="gsc_prf_ila")

    for a in html_soup.find_all('a', href=True):
        a_href = a['href']
        index_org = str(a_href).find("org=")
        if  index_org >= 0:
            index_org2 = str(a).find("org=")
            start_index = str(a).find(">" , index_org2) + 1
            end_index = str(a).find("<", start_index)
            univ_new = str(a)[start_index:end_index]
            print(f"Found univ {univ_new}")

    all_a = html_soup.select('.gsc_prf_ila h')

    for a in all_a:
        print(a)

    line_to_return = str(main_author_name).replace(",", "") + "," + str(main_email) + "," + str(univ_new).replace(",", "") \
                     + "," + str(coauthor_name_conc).replace(",", "")  + "," + str(resear_int_conc).replace(",", "")
    line_to_return = line_to_return.replace("[]", "")

    return line_to_return


def random_pick_url(lst_global_url):
    # randomly pick an url for next crawling
    index = random.randrange(0, len(lst_global_url) - 1)
    url = lst_global_url[index]
    return url

if __name__ == "__main__":
    csv_line = ""
    # seed url to start with
    url = 'https://scholar.google.com/citations?user=6JeebN0AAAAJ&hl=en'
    count = 0
    try:
        while True:
            if url not in lst_already_crawled_url:
                print(f"count {count}  | crawling url {url}")
                output = crawl_author(url)
                print(output)
                # write to csv
                write_to_file(filename, output, count)
                lst_already_crawled_url.append(url)
                print("lst_global_url -> " + str(lst_global_url))
                url = random_pick_url(lst_global_url)
                count += 1
                print(f"universe list url {len(lst_global_url)}")
                if count >= LIMIT_MAX_AUTHORS:
                    break
            else:
                print("URL already crawled: " + url)
                url = random_pick_url(lst_global_url)
    except Exception as e:
        traceback.print_exc()
