import requests
from bs4 import BeautifulSoup

class n11:
    def __init__(self):
        self.url = "https://m.n11.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

    def Phone(self):
        url = self.url + "telefon-ve-aksesuarlari"

        html = requests.get(url, headers=self.headers).content
        soup = BeautifulSoup(html, "html.parser")
        print(soup.prettify())


        # phone_list = soup.find("div", {"class": "searchResults twoColumns"})
        # print(phone_list)


        # phone_list = soup.find("div", {"class": "searchResults"}).find_all("a", {"class": "product-item"})

        # for item in phone_list:
        #     name = item.find("div", {"class": "product-item-title"}).get("data-v-621c3c12")
        #     price = item.find("div", {"class": "price-currency"}).get("data-v-621c3c12")
        #     print(name, price)




#menü
shopping = n11()
while True:
    choice = input("1-Phone\n2-Exit\n")

    if choice == '1':
        shopping.Phone()

    if choice == '2':
        break