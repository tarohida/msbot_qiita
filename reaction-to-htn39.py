import sys
import random
import pprint

sys.path.append('/usr/lib/python3.6/site-packages/')

from mastodon import Mastodon

#initialize
mastodon = Mastodon(
    client_id="/home/taro/msbot_qiita/account_info/cred.txt",
    access_token="/home/taro/msbot_qiita/account_info/auth.txt",
    api_base_url = "https://qiitadon.com")

#get_local_toot
toots = mastodon.timeline_local(limit=10)

#reaction
for toot in toots:
    #pprint.pprint(toot)
    #print(toot.content)
    if toot.account.id == 45761:
        continue

    if toot.content == '<p>ﾊﾂﾈﾐｸ</p>':
        mastodon.status_reblog(toot.id)
        mastodon.status_favourite(toot.id)
