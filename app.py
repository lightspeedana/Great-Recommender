import requests
from bs4 import BeautifulSoup

for x in range (0, 1000):
    r = requests.get("https://myanimelist.net/anime/"+str(x)+"/")
    if r.status_code == 404:
        print("No title at "+str(x))
    else:
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.find("h1", class_="title-name h1_bold_none")
        anime_name = title.find("strong").contents[0]
        print(str(x)+" - "+anime_name)
