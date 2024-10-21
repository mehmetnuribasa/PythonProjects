from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)
driver.maximize_window()

searchInput = driver.find_element(By.CLASS_NAME, 'header-search-button')
searchInput.click()
time.sleep(1)

writingInput = driver.find_element(By.ID, 'query-builder-test')
writingInput.send_keys("python")
time.sleep(1)

writingInput.send_keys(Keys.ENTER)
time.sleep(4)

# #gets the source of page and we can convert the beautıfulsoup object..
# result = driver.page_source
# print(result)


# #like sleep()
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, 'Box-sc-g0xbh4-0'))
# )


result = driver.find_elements(By.CSS_SELECTOR, '.Box-sc-g0xbh4-0 h3 a')
for i in result:
    print(i.text)

driver.close()
