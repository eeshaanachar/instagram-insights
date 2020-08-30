import sqlite3
from concurrent.futures import ThreadPoolExecutor
from instagram_bot import InstagramBot


connection = sqlite3.connect('cache.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS HASHTAGS (KEYWORD TEXT, HASHTAG TEXT, DATE TEXT DEFAULT CURRENT_TIMESTAMP)')

bot = InstagramBot('foo')

for keyword in input('> ').split():
    with ThreadPoolExecutor() as executor:
        list_list_hashtag = executor.map(bot.getPostHashtags, bot.getTopHashtagPosts(keyword))
    for list_hashtag in list_list_hashtag:
        for hashtag in list_hashtag:
            cursor.execute('INSERT INTO HASHTAGS VALUES (?, ?, DATETIME("NOW"))', (keyword, hashtag))

connection.commit()
connection.close()
