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

kanji_to_search_for = "裏"
subpaths_to_exclude = ["/archive/text"]
file_to_write_name = "phrases_for_{}.txt".format(kanji_to_search_for)


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

for a in soup.find("table", {"class": "maintable"}).find_all("a"):
    sub_path = a["href"]
    if sub_path not in subpaths_to_exclude:
        load_page(base_url + sub_path)

keys = letters_dict
f = open(file_to_write_name, "w")
for key in keys:
    f.write(key.encode('utf8'))
    f.write(' \n')
    print key
f.close()
