from mastodon import Mastodon

#initialize
mastodon = Mastodon(
    client_id="./account_info/cred.txt",
    access_token="./account_info/auth.txt",
    api_base_url = "https://qiitadon.com")

#get_local_toot
toots = mastodon.timeline_local(limit=10)

#reaction
for toot in toots:
    if toot.account.id == 45761:
        continue

    if toot.content == '<p>ﾊﾂﾈﾐｸ</p>':
        mastodon.status_reblog(toot.id)
        mastodon.status_favourite(toot.id)

