from selenium import webdriver
from time import sleep


class InstagramBot:

    def __init__(self, username, password=None, bot_username=None, headless=True, max_wait=10, scroll_delay=0.5):
        self.username = username  
        chrome_options = webdriver.chrome.options.Options()
        if headless:
            chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
        self.driver.implicitly_wait(max_wait)
        self.SCROLL_DELAY = scroll_delay
        if password:
            print('Logging in...')
            self.driver.get('https://www.instagram.com/accounts/login')
            self.driver.find_element_by_name('username').send_keys(bot_username if bot_username else username)
            self.driver.find_element_by_name('password').send_keys(password + webdriver.common.keys.Keys.RETURN)
            self.driver.find_elements_by_class_name('ABCxa')

    def __scan(self):
        scroll_box = self.driver.find_element_by_class_name('isgrP')
        last_height, height = 0, 1
        while last_height != height:
            sleep(self.SCROLL_DELAY)
            last_height = height
            height = self.driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_box)
        user_links = scroll_box.find_elements_by_tag_name('a')
        return {user.text for user in user_links}

    def getFollowersList(self):
        print('Getting Followers...')
        self.driver.get('https://www.instagram.com/' + self.username)
        self.driver.find_element_by_partial_link_text('followers').click()
        return self.__scan()

    def getFollowingList(self):
        print('Getting Following...')
        self.driver.get('https://www.instagram.com/' + self.username)
        self.driver.find_element_by_partial_link_text('following').click()
        return self.__scan()

    def getLatestPosts(self, count=9):
        urls = list()        
        self.driver.get('https://www.instagram.com/' + self.username)
        a_tags = self.driver.find_element_by_tag_name('article').find_elements_by_tag_name('a')[:count]
        for a_tag in a_tags:
            urls.append(a_tag.get_attribute('href'))
        return urls

    def getPostLikeList(self, url):
        print('Scanning ' + url)
        self.driver.get(url)
        sleep(1)
        self.driver.find_element_by_css_selector('.Nm9Fw button').click()
        scroll_box = self.driver.find_element_by_css_selector('div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div')
        last_height, height, names = 0, 1, set()
        while last_height != height:
            sleep(self.SCROLL_DELAY)
            names.update(aTag.text for aTag in scroll_box.find_elements_by_tag_name('a'))
            last_height = height
            height = self.driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_box)
        return names
