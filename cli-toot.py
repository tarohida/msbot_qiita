import sys
import random

sys.path.append('/usr/lib/python3.6/site-packages/')

from mastodon import Mastodon
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('toot', type=str)
args = parser.parse_args()

mastodon = Mastodon(
	client_id="./account_info/cred.txt",
	access_token="./account_info/auth.txt",
	api_base_url = "https://qiitadon.com") #インスタンス

mastodon.toot(args.toot)

