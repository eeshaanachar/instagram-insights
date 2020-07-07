import time
import pyautogui as gui
from selenium import webdriver

def scroll():
    for i in range(50): #adjust as per the number of followers/following
        gui.moveTo(500,500) #adjust according to display resolution
        gui.scroll(-300) #adjust as per loading speed
        time.sleep(0.2) #adjust as per loading speed

username = 'rms13607' #input('Username ')
password = 'imsosorry' #input('Password ')

driver = webdriver.Chrome('.\chromedriver')
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(1)

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
time.sleep(2)

driver.get('https://www.instagram.com/achareeshaan') #'https://www.instagram.com/'+username
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
scroll()
followers = set()
a_tags = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div').find_elements_by_tag_name('a')
for a_tag in a_tags:
    followers.add(a_tag.get_attribute('title'))

driver.get('https://www.instagram.com/achareeshaan') #'https://www.instagram.com/'+username
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
scroll()
following = set()
a_tags = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div').find_elements_by_tag_name('a')
for a_tag in a_tags:
    following.add(a_tag.get_attribute('title'))

driver.quit()
print("These accounts don't follow you back")
for account in following-followers:
    print(account)
input()
