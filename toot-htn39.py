from mastodon import Mastodon
from libs.IsHatsuneBirthdayService import IsHatsuneBirthdayService as Hatsune
import random

debug = True
if debug is True:
    visibility = 'direct'
else:
    visibility = None

mastodon = Mastodon(
    client_id="./account_info/cred.txt",
    access_token="./account_info/auth.txt",
    api_base_url="https://qiitadon.com")

if Hatsune().is_birthday():
    message = 'ﾊﾋﾟﾊﾞﾐｸ :birthday:'
    mastodon.status_post(
        message,
        visibility=visibility
    )

num = random.randrange(1, 100)
if num <= 39:
    message = 'ﾊﾂﾈﾐｸ'
    mastodon.status_post(
        message,
        visibility=visibility
    )
