import requests
import json
from config import API_TOKEN

class FilmArchives:
    def __init__(self):
        self.url = "https://api.themoviedb.org/3/"
        self.token = API_TOKEN

    def mostPopular(self):
        url = f"{self.url}movie/popular?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, headers=headers)
        # print(response.text)
        return response.json()


    def SearchMovie(self, query):
        url = f"{self.url}search/keyword?query={query}&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, headers=headers)
        # print(response.text)
        return response.json()


#Menü
archives = FilmArchives()
while True:
    choice = input("1-Most Popular Films\n2-Search a Movie\n3-Exit\n")

    if choice == '1':
        result = archives.mostPopular()
        
        for i in result["results"]:
            print(i["title"])


    if choice == '2':
        keyword = input("Keyword: ")
        result = archives.SearchMovie(query=keyword)

        pageNumber = result["total_pages"]
        print(f"Total number of pages is {pageNumber}")
        print("Page 1:")
        for i in result["results"]:
            print(i["name"])


    if choice == '3':
        break