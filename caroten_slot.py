import sys
import random
import time 

sys.path.append('/usr/lib/python3.6/site-packages/')

from mastodon import Mastodon

class Carotenslot:

	nums = ['ぜろ','わん','つー','すりー','ふぉー','ふぁいぶ','しっくす','せぶん','えいと','ないん','てん']
	caro = 'かろ'

	def __init__(self):
		self.mastodon = Mastodon(
			client_id="/home/mutsu/python/msbot_qiita/account_info/cred.txt", 
			access_token="/home/mutsu/python/msbot_qiita/account_info/auth.txt",
			api_base_url = "https://qiitadon.com") #インスタンス

	def run(self, delay):
		self.mastodon.toot('carotenslot発動！！')
		time.sleep(delay)
		self.mastodon.toot(self.caro + 'てん' + '!')
		selected_nums = random.sample(self.nums,2)

		for selected_num in selected_nums:
			time.sleep(delay)
			self.mastodon.toot(self.caro + selected_num + '!')
			if selected_num != 'かろてん':
				return False 
		
		return True

			
	def congratulations(self):
		self.mastodon.toot('おめでとう！！')

client_id="/home/mutsu/python/msbot_qiita/account_info/cred.txt"
access_token="/home/mutsu/python/msbot_qiita/account_info/auth.txt"
api_base_url = "https://qiitadon.com"

delay = 3

carotenslot = Carotenslot()

result = carotenslot.run(delay)

if result:
	carotenslot.congratulations()

	
#	mastodon.toot("ﾊﾂﾐﾈｸ") #ここを変える
# mastodon.toot("ﾊ゛ﾂ゛ﾈ゛ﾐ゛ｸ゛") #ここを変える
