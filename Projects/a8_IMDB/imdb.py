import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
url_simple = "https://www.imdb.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# html = requests.get(url).text
html = requests.get(url, headers=headers).content

soup = BeautifulSoup(html, "html.parser")

movie_list = soup.find("ul", {"class": "ipc-metadata-list"}).find_all("li", limit=10)

for item in movie_list:
    movieName = item.find("h3", {"class": "ipc-title__text"}).text
    # movieName = item.h3.text
    imdb_rating = item.find("span", {"class": "ipc-rating-star"}).text
    link = item.find("a", {"class": "ipc-title-link-wrapper"}).get("href")
    print(movieName, imdb_rating)
    print(url_simple + link)