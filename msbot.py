import sys
import random

sys.path.append('/usr/lib/python3.6/site-packages/')

from mastodon import Mastodon

mastodon = Mastodon(
	client_id="/root/python/msbot_qiita/account_info/cred.txt", 
	access_token="/root/python/msbot_qiita/account_info/auth.txt",
	api_base_url = "https://qiitadon.com") #インスタンス
num = random.randrange(1, 10)
if num <= 3:
	mastodon.toot("ﾊﾂﾈﾐｸ") #ここを変える
elif 3 < num <= 4:
	mastodon.toot("ﾊﾐﾂﾈｸ") #ここを変える
