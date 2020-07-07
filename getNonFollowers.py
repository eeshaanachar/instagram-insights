from time import sleep
from selenium import webdriver


def scan():
    sleep(1)
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        sleep(1)
        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)
    names = scroll_box.find_elements_by_tag_name('a')
    return {name.text for name in names}


chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver', options = chrome_options)

print('Logging in...')
driver.get('https://www.instagram.com/accounts/login/?next=%2Fachareeshaan')
sleep(1)

driver.find_element_by_name('username').send_keys('rms13607')
driver.find_element_by_name('password').send_keys('imsosorry')
driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(3)

print('Scanning Followers...')
driver.find_element_by_xpath('//a[contains(@href,"/followers")]').click()
followers = scan()
    
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()

print('Scanning Following...')
driver.find_element_by_xpath('//a[contains(@href,"/following")]').click()
following = scan()

driver.quit()

print("Accounts that don't follow you back")
for account in following-followers:
    print(account)

input()