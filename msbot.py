import sys
import random

sys.path.append('/usr/lib/python3.6/site-packages/')

from mastodon import Mastodon

mastodon = Mastodon(
	client_id="/root/python/msbot_qiita/account_info/cred.txt", 
	access_token="/root/python/msbot_qiita/account_info/auth.txt",
	api_base_url = "https://qiitadon.com") #インスタンス
num = random.randrange(1, 100)
if num <= 39:
#	mastodon.toot("ブチ殺すぞ…… kill you")
	mastodon.toot("ﾊﾂﾈﾐｸ") #ここを変える
#elif 4 < num <= 5:
#	mastodon.toot("ﾊﾐﾂﾈｸ") #ここを変える
#elif 5 < num <= 6:
#	mastodon.toot("ﾊﾂﾐﾈｸ") #ここを変える
# mastodon.toot("ﾊ゛ﾂ゛ﾈ゛ﾐ゛ｸ゛") #ここを変える
