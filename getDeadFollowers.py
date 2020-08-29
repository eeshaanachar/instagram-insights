from instagram_bot import InstagramBot
from secrets import Credentials


bot = InstagramBot(Credentials.username, Credentials.bot_password, Credentials.bot_username)
followers = bot.getFollowersList()
print(len(followers), 'followers found')

posts_ignored = dict(zip(followers, [0]*len(followers)))
for url in bot.getLatestPosts():
    try:
        likes = bot.getPostLikeList(url)
    except:
        continue
    print(len(likes), 'likes found')
    for name in followers - likes:
        posts_ignored[name] += 1

for item in sorted(posts_ignored.items(), key=lambda x : x[1]):
    print(item)
