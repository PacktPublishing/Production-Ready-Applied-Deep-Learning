# Collect Google Scholar authors html pages from web and convert to CSV
from bs4 import BeautifulSoup
from requests import get

url = 'https://scholar.google.com/citations?user=6JeebN0AAAAJ&hl=en'
# http request
response = get(url)
# inside response, we have text field/parameter
html_soup = BeautifulSoup(response.text, 'html.parser')
# print(html_soup.prettify())

############## Research Interest
lst_resear_int = []
lst_coauthors_link = []

# For loop to iterate each of the href attribute value found inside <a> tag
for a in html_soup.find_all('a', href=True):

    # print("Found the URL (ALL):", a['href'])

    ######## research interest
    temp1 = str(a).find("mauthors=label:") # .find is used to do "substring finding"..
    if temp1 >= 0:
        print("RI: Found the URL:", a['href'])
        ri = str(a['href']).replace("/citations?view_op=search_authors&hl=en&oe=ASCII&mauthors=label:", "")
        lst_resear_int.append(ri)

        print("temp1: " + str(temp1) + " current url:" + a['href'])

    ######## co-author related
    temp2 = str(a).find("/citations?user=")  # .find is used to do "substring finding"..
    if temp2 >= 0:
        print("Co-Author: Found the URL:", a['href'])
        ca = "https://scholar.google.com" + str(a['href'])
        lst_coauthors_link.append(ca)

        print("temp2: " + str(temp2) + " current url:" + a['href'])

print("-------------")
print("list research interests:" + str(lst_resear_int))
print("list co-authors link:" + str(lst_coauthors_link))

############## Name
main_author_name = html_soup.select('div#gsc_prf_in')[0].get_text()
print(main_author_name)

############## Get official email id


main_email = html_soup.select('div#gsc_prf_ivh')[0].get_text()
main_email = main_email.replace("Verified email at ", "")
print(main_email)

############## University affiliation
univ = html_soup.find_all('href', class_="gsc_prf_ila")

all_a = html_soup.select('.gsc_prf_ila h')

for a in all_a:
    print(a)

print(univ)
