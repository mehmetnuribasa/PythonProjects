from userInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.repositories = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element(By.XPATH, "//*[@id='login_field']")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='password']")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()
        time.sleep(4)

    def getRepository(self):
        self.browser.get(f"https://github.com/{self.username}?tab=repositories")
        time.sleep(2)

        repos = self.browser.find_elements(By.CSS_SELECTOR, ".col-10 h3 a")

        for i in repos:
            self.repositories.append(i.text)

app = Github(username, password)
app.signIn()
app.getRepository()
print(app.repositories)
