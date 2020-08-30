import sqlite3
from random import sample


keys = input('> ').split()
counts = map(int, input('> ').split())
hashtags = set()

with sqlite3.connect('cache.db') as connection:
    cursor = connection.cursor()
    for key, count in zip(keys, counts):
        results = connection.execute(f'SELECT HASHTAG FROM HASHTAGS WHERE KEYWORD=? GROUP BY HASHTAG ORDER BY COUNT(*) DESC', (key, )).fetchmany(count * 3 // 2)
        for result in sample(results, min(len(results), count)):
            hashtags.add('#' + result[0])

count = 0
with open('output.txt', 'w') as file_handle:
    for hashtag in hashtags:
        try:
            file_handle.write(hashtag + ' ')
            count += 1
        except UnicodeEncodeError:
            continue
print(count)
