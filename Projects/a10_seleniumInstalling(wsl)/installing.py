from selenium import webdriver

chrome_binary_path = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"    #chrome file in windows
chromedriver_path = "/mnt/c/Users/mehme/Folder/Python/Projects/a10_seleniumInstalling(wsl)/chromedriver" #chromedriver file in wsl


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_path


driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

url = "http://sadikturan.com"

driver.get(url)