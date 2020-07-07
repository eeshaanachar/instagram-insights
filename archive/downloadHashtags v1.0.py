import urllib
from selenium import webdriver
from bs4 import BeautifulSoup

keys = input().split()

for key in keys:
    
    urls = list()
    hashtags = list()
    tempset = set()
    print('\nFinding Posts on',key+'...')
    
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.instagram.com/explore/tags/'+key)
    a_tags = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article').find_elements_by_tag_name('a')    
    for a_tag in a_tags:
        urls.append(a_tag.get_attribute('href'))
    driver.quit()

    print(len(urls),'Posts found. Extracting hashtags...')
    for url in urls:
        try:
            connection = urllib.request.urlopen(url)
            soup = BeautifulSoup(connection.read(), 'html.parser')
            connection.close()
            html_tags = soup.find_all('meta', attrs={'property': 'instapp:hashtags'})
            for tag in html_tags:
                hashtags.append(tag.get('content').lower())
            print('Extracted from post',urls.index(url)+1)
        except:
            print('Post',urls.index(url)+1,'failed')
            connection.close()

    for hashtag in hashtags:
        if hashtags.count(hashtag) > 4 or (key in hashtag and hashtags.count(hashtag) > 2):
            tempset.add(hashtag)
            
    try:
        file = open('./Collections/'+key+'.txt')
        hashtags = file.read().split()
        file.close()
    except FileNotFoundError:
        hashtags = list()
        file = open('./Collections/__index__.txt','a')
        file.write(key+' ')
        file.close()

    print(len(tempset),'relavent hashtags found. Verifying and adding to Collection...')
    for hashtag in tempset:
        try:
            if hashtag not in hashtags:
                connection = urllib.request.urlopen('https://www.instagram.com/explore/tags/'+hashtag)
                soup = BeautifulSoup(connection.read(), 'html.parser')
                connection.close()
                posts = soup.find_all('meta', attrs={'name': 'description'})[0].get('content').split()[0]
                posts_int = float(posts.replace('b', 'e9').replace('m', 'e6').replace('k', 'e3'))
                if posts_int >= 100000 and posts_int <= 250000000:
                    hashtags.append(hashtag)
                    print(hashtag,'added')
        except:
            pass

    file = open('./Collections/'+key+'.txt','w')
    file.write(' '.join(hashtags)+' ')
    file.close()
input('Done>')
