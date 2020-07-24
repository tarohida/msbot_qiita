qiitadonで遊んでるやつ。 
crondで叩けば遊べる 

# pre-install

```
sudo apt-get install python3-venv
```

# install

```
git clone https://github.com/taro-hida/msbot_qiita.git
cd ./msbot_qiita/

python3 -m venv venv
source venv/bin/activate
python3 -m pip install Mastodon.py

mkdir ./account_info
touch ./account_info/{auth,cred}.txt
```

`account_info`ディレクトリ以下のファイルは空ファイルだとエラーが出るので、Mastodon.pyのドキュメントを確認してsetupする

テスト実行して、エラーが出力されないか確認する。
確認ができたら、以下実行してcrondで実行されるようにする。

ユーザがubuntu以外の場合は、`msbot-qiita-cron`の修正が必要。

```
sudo cp msbot-qiita-cron /etc/cron.d/
```

