from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ScrollOrigin


class instagram:
    def __init__(self, userName, password):
        #Runs the chromedriver with english language.
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_argument("--lang=en-US")

        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.browser.minimize_window()
        self.username = userName
        self.password = password
        self.followers = []
        self.followings = []
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        inputUsername = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        inputPassword = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        inputUsername.send_keys(self.username)
        inputPassword.send_keys(self.password)

        #sign in button
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()
        time.sleep(10)

        #If could not log in.. successully
        if self.browser.current_url == "https://www.instagram.com/accounts/login/":
            error = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/span")
            print('\n' + error.text)
            self.signOut()
            raise Exception

    def signOut(self):
        self.browser.close()


    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(4)

        try:
            followersLink = self.browser.find_element(By.PARTIAL_LINK_TEXT, "follower")
            followersLink.click()
            time.sleep(4)

            followerCatalog = self.browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")
            followerList = followerCatalog.find_elements(By.CSS_SELECTOR, ".x1dm5mii")

            #Find the total follower numbers
            followerNumber = int(followersLink.find_element(By.CSS_SELECTOR, "span").text)

            #Method1
            action = webdriver.ActionChains(self.browser)
            while True:
                counter = len(followerCatalog.find_elements(By.CSS_SELECTOR, ".x1dm5mii"))
                print(f"Follower Count: {counter}")

                if(counter < followerNumber-1):
                    #Scrolling down..
                    action.scroll_from_origin(ScrollOrigin.from_element(followerCatalog), 0, 1000).perform()
                    
                    # followerCatalog.click()
                    # action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    
                    # action.send_keys(Keys.PAGE_DOWN).perform()
                    time.sleep(2)
                else:
                    break

            #Method2
            # in this method, we dont know how many followers have, we only scrolling down to the end.
            # followerCount = len(followerList)
            # print(f"Follower Count: {followerCount}")

            # action = webdriver.ActionChains(self.browser)
            # while True:
            #     followerCatalog.click()
            #     action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            #     time.sleep(2)
                
            #     newCount = len(followerCatalog.find_elements(By.CSS_SELECTOR, ".x1dm5mii"))
                
            #     if followerCount != newCount:
            #         followerCount = newCount
            #         print(f"Follower Count: {followerCount}")
            #     else:
            #         break
            
            followerList = followerCatalog.find_elements(By.CSS_SELECTOR, ".x1dm5mii a span")
            for i in followerList:
                self.followers.append(i.text)
        
        except Exception as e:
            print(e)

    def writeFollowers(self):
        for item in self.followers:
            print(item)
        print(f"Takipçi Sayisi: {len(self.followers)}\n")


    def getFollowings(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(4)

        try:
            followingLink = self.browser.find_element(By.PARTIAL_LINK_TEXT, "following")
            followingLink.click()
            time.sleep(4)

            followingCatalog = self.browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div")
            followingList = followingCatalog.find_elements(By.CSS_SELECTOR, ".x1dm5mii")

            #Find the total following numbers
            followingNumber = int(followingLink.find_element(By.CSS_SELECTOR, "span").text)

            # Method1
            action = webdriver.ActionChains(self.browser)
            while True:
                counter = len(followingCatalog.find_elements(By.CSS_SELECTOR, ".x1dm5mii"))
                print(f"Following Count: {counter}")

                if(counter < followingNumber-1):
                    # # Get the height of the followerCatalog element (Not Used Only Example)
                    # followerCatalogHeight = self.browser.execute_script("return arguments[0].scrollHeight", followingCatalog)
                    # scrollHeight = followerCatalogHeight
                    
                    #Scrolling down..
                    #Method1
                    action.scroll_from_origin(ScrollOrigin.from_element(followingCatalog), 0, 1000).perform()
                    
                    #Method2 (unsuccessfull)
                    # followerCatalog.click()
                    # action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    
                    #Method3 (Unsuccessfull)
                    # action.send_keys(Keys.PAGE_DOWN).perform()
                    time.sleep(2)
                else:
                    break
            
            followingList = self.browser.find_elements(By.CSS_SELECTOR, ".x1dm5mii a span")
            for i in followingList:
                self.followings.append(i.text)

        except Exception as e:
            print(e)


    def writeFollowings(self):
        for item in self.followings:
            print(item)
        print(f"Takip Sayisi: {len(self.followings)}\n")


    def followUser(self, username):
        try:
            self.browser.get(f"https://www.instagram.com/{username}/")
            time.sleep(2)

            followButton = self.browser.find_element(By.TAG_NAME, "button")
            
            if followButton.text != 'Following':
                followButton.click()
                time.sleep(2)
                print(f"{username} hesabi artik takip ediliyor.\n")
            else:
                print(f"{username} hesabini zaten takip ediyorsun.\n")
        
        except Exception as e:
            print(e)


    def unFollowUser(self, username):
        try:
            self.browser.get(f"https://www.instagram.com/{username}/")
            time.sleep(2)

            followButton = self.browser.find_element(By.TAG_NAME, "button")

            if followButton.text == 'Following':
                followButton.click()
                time.sleep(2)
                # self.browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[1]/div/div/span").click()       
                self.browser.find_element(By.XPATH, "//span[text()='Unfollow']").click()
                # self.browser.find_element(By.XPATH, "//div[@data-testid='tweet']/div[2]/div[2]")    #(Not Used) it is only example. there is an usage like this way.
                time.sleep(2)
                print(f"{username} hesabi takipten çikildi.\n")
            else:
                print(f"{username} hesabini zaten takip etmiyorsun.\n")

        except Exception as e:
            print(e)
    

    def notFollowYou(self):
        if len(self.followers) == 0:
            self.getFollowers()
        if len(self.followings) == 0:
            self.getFollowings()

        counter = 0
        for item in self.followings:
            if not item in self.followers:
                counter += 1
                print(item)
        print(f"Takip etmeyenler: {counter}")
        print("\n")

    def youDontFollow(self):
        if len(self.followers) == 0:
            self.getFollowers()
        if len(self.followings) == 0:
            self.getFollowings()

        counter = 0
        for item in self.followers:
            if not item in self.followings:
                counter += 1
                print(item)
        print(f"Takip etmediklerin: {counter}")
        print("\n")




#MENU
while True:
    print("Instagram".center(50, '.'))
    choice = input("1-Giriş Yap\n2-Çikiş\n")

    if choice == '1':
        
        while True:
            try:
                username = input("Username: ")
                password = input("password: ")
                print("Giriş Yapiliyor..")
                application = instagram(username, password)
                application.signIn()

                application.getFollowers()
                application.getFollowings()
            except Exception as e:
                print(f"{e}\nTekrar Deneyin!\n")
            else:
                break

        #SUBMENU
        while True:
            choice = input("1-Takipçi Listesi\n2-Takip listesi\n3-Hesabi Takip Et\n4-Hesabi Takipten Cik\n5-Seni Takip Etmeyenler\n6-Senin Takip Etmediklerin\n7-Çikiş\n")

            if choice == '1':
                application.writeFollowers()
            elif choice == '2':
                application.writeFollowings()
            elif choice == '3':
                name = input("Kullanici Ismi: ")
                application.followUser(name)
            elif choice == '4':
                name = input("Kullanici Ismi: ")
                application.unFollowUser(name)
            elif choice == '5':
                application.notFollowYou()
            elif choice == '6':
                application.youDontFollow()
            elif choice == '7':
                application.signOut()
                break
            else:
                pass

    elif choice == '2':
        print("Çikiş Yapiliyor..")
        break
    else:
        pass

