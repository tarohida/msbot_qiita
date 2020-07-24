from mastodon import Mastodon
import random
import time

class Carotenslot:

    num1 = ['ぜろ','わん','つー','すりー','ふぉー','ふぁいぶ','しっくす','せぶん','えいと','ないん','てん']
    num2 = ['ぜろ','わん','つー','すりー','ふぉー','ふぁいぶ','しっくす','せぶん','えいと','ないん','てん']
    caro = 'かろ'

    def __init__(self):
        self.mastodon = Mastodon(
	    client_id="./account_info/cred.txt",
	    access_token="./account_info/auth.txt",
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

            if selected_num != 'てん':
                return False

        return True


    def congratulations(self):
        self.mastodon.toot('おめでとう！！')

if __name__ == "__main__":
    delay = 3
    carotenslot = Carotenslot()
    result = carotenslot.run(delay)
    if result:
        carotenslot.congratulations()

