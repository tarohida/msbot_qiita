import sys
import random

sys.path.append('/usr/lib/python3.6/site-packages/')

from mastodon import Mastodon

mastodon = Mastodon(
	client_id="/home/taro/python/msbot_qiita/account_info/cred.txt",
	access_token="/home/taro/python/msbot_qiita/account_info/auth.txt",
	api_base_url = "https://qiitadon.com") #インスタンス
num = random.randrange(1, 100)
# if num <= 39:
if num <= 0:
	mastodon.toot("ﾊﾂﾈﾐｸ") #ここを変える
