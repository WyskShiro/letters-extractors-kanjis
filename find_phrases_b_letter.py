# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup

base_url = "https://pastebin.com"
data = requests.get("https://pastebin.com/u/DocFirebird")
soup = BeautifulSoup(data.text, 'html.parser')
letters_dict = list()


# PARAMETERS
# PARAMETERS
# PARAMETERS
# PARAMETERS

kanji_to_search_for = "観"
subpaths_to_exclude = ["/archive/text"]
file_to_write_name = "test_phrases_for_{}.txt".format(kanji_to_search_for)
page_num = 1

# Functions
# Functions
# Functions

def add_to_list(letter):
    letters_dict.append(letter)


def load_page(url):
    print "starting this url: " + url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    for a in soup.find("div", {"class": "source"}).find_all("li"):
        if kanji_to_search_for in a.text.encode('utf-8'):
            add_to_list(a.text)


# Starts here
# Starts here
# Starts here

# Uncomment if you want to download pages again
# Uncomment if you want to download pages again
# Uncomment if you want to download pages again
# Uncomment if you want to download pages again

# for a in soup.find("table", {"class": "maintable"}).find_all("a"):
#     sub_path = a["href"]
#     if sub_path not in subpaths_to_exclude:
#         load_page(base_url + sub_path)


# Starts here if have the local txts
# Starts here if have the local txts
# Starts here if have the local txts
# Starts here if have the local txts

for i in range(1, 86):
    f = open("page_" + str(page_num), "r")
    page_num += 1
    soup = BeautifulSoup(f.read(), "html.parser")
    for a in soup.find("div", {"class": "source"}).find_all("li"):
        if kanji_to_search_for in a.text.encode('utf-8'):
            add_to_list(a.text)


keys = set(letters_dict)
f = open(file_to_write_name, "w")
for key in keys:
    f.write(key.encode('utf8'))
    f.write(' \n')
    print key
f.close()
