from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = '/home/nur/Downloads/chromedriver_linux64/chromedriver'


class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions() # chrome driveri ingilizce aciyoruz
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages': 'en,en_US'}) # istedigimiz dilleri tanimliyoruz
        
        self.browser = webdriver.Chrome(driver_path, chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://twitter.com/login')
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        btnSubmit.click()
        self.browser.maximize_window()
        time.sleep(2)


    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)


        loopCounter = 0
        last_height = self.browser.execute_script('return document.documentElement.scrollBar')
        while True:
            if loopCounter>5:
                break
            self.browser.execute_script('window.scrollTo(0,document.documentElement.scrollBar)')
            time.sleep(2)
            new_height = self.browser.execute_script('return document.documentElement.scrollBar')
            if(last_height == new_height):
                break
            last_height = new_height

        list = self.browser.find_elements_by_xpath('//div[@data-testid="tweet"]/div[2]/div[2]')
        for i in list:
            print(i.text)
            print('***********')

twitter = Twitter(username,password)

# login
twitter.signIn()
twitter.search('python')