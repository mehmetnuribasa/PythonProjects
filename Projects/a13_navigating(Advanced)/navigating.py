from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class github:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "http://github.com"
        self.elementsName = []

    def running(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        searchButton = self.driver.find_element(By.CLASS_NAME, 'header-search-button')
        searchButton.click()
        time.sleep(1)

        SearchInput = self.driver.find_element(By.ID, 'query-builder-test')
        SearchInput.send_keys("python")
        time.sleep(1)

        SearchInput.send_keys(Keys.ENTER)
        time.sleep(4)

        self.getResults()
        self.otherPage()
        self.otherPage()


    def getResults(self):
        result = self.driver.find_elements(By.CSS_SELECTOR, '.Box-sc-g0xbh4-0 h3 a')
        for i in result:
            self.elementsName.append(i.text)
    
    def printResults(self):
        for item in self.elementsName:
            print(item)


    def otherPage(self):
        pagination_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[5]/div/nav/div")
        items = pagination_button.find_elements(By.CSS_SELECTOR, "a")

        # items = self.driver.find_elements(By.CSS_SELECTOR, ".Pagination__PaginationContainer-sc-cp45c9-1.Box-sc-g0xbh4-0 a")

        for item in items:
            if(item.get_attribute("aria-label") == "Next Page"):
                item.click()
                time.sleep(4)
                self.getResults()
            else:
                continue




application = github()
application.running()
application.printResults()
