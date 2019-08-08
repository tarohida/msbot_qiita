#!/usr/bin/python

from mastodon import Mastodon

url = 'https://qiitadon.com'

Mastodon.create_app("t-bot", #クライアント名
	api_base_url = url,
	to_file = "../account_info/cred.txt"
)
mastodon = Mastodon(
	client_id="../account_info/cred.txt",
	api_base_url = url
)
mastodon.log_in(
	"", #ログインメールアドレス
	"", #パスワード
	to_file="../account_info/auth.txt"
)
