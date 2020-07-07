from selenium import webdriver
from selenium.webdriver.chrome.options import Options

keywords = input('Enter space separated keywords to search for hashtags > ').split()
xpath = '//*[@id="react-root"]/section/main/header/div[2]/div[2]/span'
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver', options = chrome_options)

for keyword in keywords:
    i = 0
    hashtags = [keyword]

    # try to run the loop 5 times
    while i<len(hashtags) and i<5:
        driver.get('https://www.instagram.com/explore/tags/' + hashtags[i])
        # the releated tags may not be available
        try:
            hashtags.extend(driver.find_element_by_xpath(xpath).text.split('#')[1:])    # first element of list is 'Related Tags', hence eliminate it
            hashtags = list(dict.fromkeys(hashtags))    # eliminate duplicates
        except:
            pass
        i += 1

    # if file found, read contents; if not, create entry in __index__ file
    try:
        file = open('./cache/' + keyword + '.txt')
        collection = set(file.read().split())
        file.close()
    except FileNotFoundError:
        collection = set()
        file = open('./cache/__index__.txt', 'a')
        file.write(keyword + ' ')
        file.close()

    # add to file
    collection.update(hashtags)
    file = open('./cache/' + keyword + '.txt','w')
    try:
        file.write(' '.join(collection) + ' ')
    except UnicodeEncodeError:
        pass
    file.close()
    
    print('Found', hashtags, 'for', keyword)
    
driver.quit()
input('Done')