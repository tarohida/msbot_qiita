from mastodon import Mastodon
from libs.IsHatsuneBirthdayService import IsHatsuneBirthdayService as Hatsune
import random

mastodon = Mastodon(
    client_id="./account_info/cred.txt",
    access_token="./account_info/auth.txt",
    api_base_url="https://qiitadon.com")

if Hatsune().is_birthday():
    mastodon.toot("ﾊﾋﾟﾊﾞﾐｸ")

num = random.randrange(1, 100)
if num <= 39:
    mastodon.toot("ﾊﾂﾈﾐｸ")
