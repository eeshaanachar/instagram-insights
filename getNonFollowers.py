from instagram_bot import InstagramBot
from secrets import Credentials


bot = InstagramBot(Credentials.username, Credentials.bot_password, Credentials.bot_username)
print(bot.getFollowingList() - bot.getFollowersList())
