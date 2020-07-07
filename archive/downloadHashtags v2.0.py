import urllib
from selenium import webdriver
from bs4 import BeautifulSoup

def find_hashtags(keyword):
    urls = list()
    hashtags = list()
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.instagram.com/explore/tags/'+keyword)
    a_tags = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article').find_elements_by_tag_name('a')
    for a_tag in a_tags:
        urls.append(a_tag.get_attribute('href'))
    driver.quit()
    for url in urls:
        try:
            connection = urllib.request.urlopen(url)
            soup = BeautifulSoup(connection.read(), 'html.parser')
            connection.close()
            html_tags = soup.find_all('meta', attrs={'property': 'instapp:hashtags'})
            for tag in html_tags:
                hashtags.append(tag.get('content').lower())
        except:
            pass
    return {hashtag for hashtag in hashtags if hashtags.count(hashtag) > 6 or keyword in hashtag and hashtags.count(hashtag) > 3}

def add_to_collection(keyword, hashtags):
    try:
        file = open('./Collections/'+keyword+'.txt')
        collection = file.read().split()
        file.close()
    except FileNotFoundError:
        collection = list()
        file = open('./Collections/__index__.txt','a')
        file.write(keyword+' ')
        file.close()
    for hashtag in hashtags:
        try:
            if hashtag not in collection:
                connection = urllib.request.urlopen('https://www.instagram.com/explore/tags/'+hashtag)
                soup = BeautifulSoup(connection.read(), 'html.parser')
                connection.close()
                posts = soup.find_all('meta', attrs={'name': 'description'})[0].get('content').split()[0]
                posts_int = float(posts.replace('b', 'e9').replace('m', 'e6').replace('k', 'e3'))
                if posts_int >= 100000 and posts_int <= 100000000:
                    collection.append(hashtag)
                    print('#'+hashtag+' added to Collection')
        except:
            pass
    file = open('./Collections/'+keyword+'.txt','w')
    file.write(' '.join(collection)+' ')
    file.close()

keywords = input('> ').split()
for keyword in keywords:
    print('\nWorking on '+keyword+'...')
    hashtags = [keyword]
    for i in range(10):
        try:
            if keyword in hashtags[i]:
                hashtags.extend(find_hashtags(hashtags[i]))
                hashtags = list(dict.fromkeys(hashtags))
        except IndexError:
            break
    add_to_collection(keyword, hashtags)
print('Done')
input()
