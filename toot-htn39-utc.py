from mastodon import Mastodon
import random

mastodon = Mastodon(
    client_id="./account_info/cred.txt",
    access_token="./account_info/auth.txt",
    api_base_url="https://qiitadon.com")
num = random.randrange(1, 1000)
if num <= 39:
    mastodon.toot("hatsune miku (UTC)")
