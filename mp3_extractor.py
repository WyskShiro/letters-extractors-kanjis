import urllib
import requests
from bs4 import BeautifulSoup


base_url = "https://downloads.khinsider.com"
url_with_osts = "{}/game-soundtracks/album/yu-gi-oh-duel-monsters-gx-sound-duel-vol-i".format(base_url)
subpaths_to_exclude = []

data = requests.get(url_with_osts)
soup = BeautifulSoup(data.text, 'html.parser')


def load_page(url, name):
    print "starting this url: " + url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    audio = soup.find("audio")
    urllib.urlretrieve(audio["src"], "{}.mp3".format(name))


is_first = True
for tr in soup.find("table", {"id": "songlist"}).find_all("tr"):
    if is_first:
        is_first = False
        continue
    a = tr.find("a")
    name = tr.find("td", {'class':"clickable-row"}).text
    sub_path = a["href"]
    if sub_path not in subpaths_to_exclude:
        load_page(base_url + sub_path, name)


