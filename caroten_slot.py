import sys
import random
import time

sys.path.append('/usr/lib/python3.6/site-packages/')

from mastodon import Mastodon

class Carotenslot:

    num1 = ['ぜろ','わん','つー','すりー','ふぉー','ふぁいぶ','しっくす','せぶん','えいと','ないん','てん']
    num2 = ['ぜろ','わん','つー','すりー','ふぉー','ふぁいぶ','しっくす','せぶん','えいと','ないん','てん']
    caro = 'かろ'

    def __init__(self):
        self.mastodon = Mastodon(
	    client_id="/home/taro/python/msbot_qiita/account_info/cred.txt",
	    access_token="/home/taro/python/msbot_qiita/account_info/auth.txt",
            api_base_url = "https://qiitadon.com") #インスタンス

    def run(self, delay):
        self.mastodon.toot('かろてんすろっと発動！！')
        time.sleep(delay)
        self.mastodon.toot(self.caro + 'てん' + '!')
        selected_nums = random.sample(self.num1,1)
        selected_nums.extend(random.sample(self.num2,1))

        for selected_num in selected_nums:
            time.sleep(delay)
            self.mastodon.toot(self.caro + selected_num + '!')
            #print(self.caro + selected_num + '!')

            if selected_num != 'てん':
                return False

        return True


    def congratulations(self):
        self.mastodon.toot('おめでとう！！')
        #print('おめでとう！！')

delay = 3

carotenslot = Carotenslot()

result = carotenslot.run(delay)

if result:
    carotenslot.congratulations()


#       mastodon.toot("ﾊﾂﾐﾈｸ") #ここを変える
# mastodon.toot("ﾊ゛ﾂ゛ﾈ゛ﾐ゛ｸ゛") #ここを変える
