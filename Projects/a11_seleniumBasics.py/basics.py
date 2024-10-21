from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

url = "http://github.com"
driver.get(url)


time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github_homepage.png")
print(driver.title)


url2 = "http://github.com/sadikturan"
driver.get(url2)
print(driver.title)

if "sadikturan" in driver.title:
    driver.save_screenshot("github_st.png")

time.sleep(2)

driver.back()
# driver.forward()
time.sleep(2)
driver.close()

