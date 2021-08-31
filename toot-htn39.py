from mastodon import Mastodon
from libs.IsHatsuneBirthdayService import IsHatsuneBirthdayService as Hatsune
import random

production = True
if production:
    visibility = None
else:
    visibility = 'direct'

mastodon = Mastodon(
    client_id="./account_info/cred.txt",
    access_token="./account_info/auth.txt",
    api_base_url="https://qiitadon.com")

if Hatsune().is_birthday():
    mastodon.status_post(
        'ﾊﾋﾟﾊﾞﾐｸ 🎂',
        visibility=visibility
    )
    exit(0)

num = random.randrange(1, 100)
if num <= 39:
    mastodon.status_post(
        'ﾊﾂﾈﾐｸ',
        visibility=visibility
    )
