import pandas
import pyautogui
from time import sleep
from selenium import webdriver

urls = list()
followers = set()
dictionary = dict()
username = 'rms13607' #input('Username ')
password = 'imsosorry' #input('Password ')

driver = webdriver.Chrome('.\chromedriver')
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_elements_by_tag_name('button')[1].click()
sleep(3)

driver.get('https://www.instagram.com/achareeshaan') #'https://www.instagram.com/'+username
sleep(1)

a_tags = driver.find_element_by_class_name('_2z6nI').find_elements_by_tag_name('a')[:15]
for a_tag in a_tags:
    urls.append(a_tag.get_attribute('href'))

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
for i in range(100): #adjust as per the number of followers/following
    pyautogui.moveTo(500,500) #adjust as per display resolution
    pyautogui.scroll(-200) #adjust as per loading speed
    sleep(0.05) #adjust as per loading speed
a_tags = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div').find_elements_by_tag_name('a')
for a_tag in a_tags:
    followers.add(a_tag.get_attribute('title'))

for url in urls:
    likes = set()
    driver.get(url)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div[2]/button').click()
    sleep(3)
    for i in range(25):
        a_tags = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div').find_elements_by_tag_name('a')
        for a_tag in a_tags:
            likes.add(a_tag.get_attribute('title'))
        pyautogui.moveTo(500,500)
        pyautogui.scroll(-500)
        sleep(0.1)
    print(len(likes))
    for follower in followers:
        if follower not in likes:
            if follower not in dictionary:
                dictionary[follower] = 1
            else:
                dictionary[follower] += 1

templist = [(keys, values)for keys,values in dictionary.items()]
df = pandas.DataFrame(templist, columns = ['User','Posts Ignored']).sort_values('Posts Ignored', ascending = False)
df.to_csv('unfollow_list.csv', index = False)

driver.quit()
input()
