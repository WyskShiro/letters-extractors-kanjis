# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import requests

base_url = "https://pastebin.com"
data = requests.get("https://pastebin.com/u/DocFirebird")
soup = BeautifulSoup(data.text, 'html.parser')

letters_dict = dict()


def add_to_dict(letter):
    try:
        letters_dict[letter] = letters_dict[letter] + 1
    except:
        letters_dict[letter] = 1


def load_page(url):
    print "starting this url: " + url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    for a in soup.find("div", {"class": "source"}).find_all("li"):
        for i in a.text:
            add_to_dict(i)


for a in soup.find("table", {"class": "maintable"}).find_all("a"):
    sub_path = a["href"]
    if sub_path != "/archive/text":
        load_page(base_url + sub_path)

dict_as_list = list()

keys = letters_dict.keys()
for k in keys:
    dict_as_list.append({"key":k, "value":letters_dict[k]})

dict_as_list.sort(reverse=True, key=lambda x: x["value"])

for k in dict_as_list:
    print k
f = open("letters_by_count.txt", "w")
for letter in dict_as_list:
    low = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    upper = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'

    if letter["key"] not in low and letter["key"] not in upper:
        f.write(letter["key"].encode('utf8') + str(letter["value"]))
        f.write(' \n')
        print letter["key"]
f.close()

