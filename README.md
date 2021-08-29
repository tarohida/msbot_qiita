# msbot_qiita

qiitadonで遊んでるやつ。 

cron で叩けば遊べる 

## setup

* python

```
sudo apt-get install python3-venv
```

* clone this repository

```
git clone ...
```

* install packages 

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -U pip
python3 -m pip install Mastodon.py
```

* create files

```
mkdir ./account_info
touch ./account_info/{auth,cred}.txt
```

`register_app.py` にログイン情報を記載した上で、以下のように実行する。

```
python register_app.py
```

テスト実行して、エラーが出力されないか確認する。

確認ができたら、以下実行して cron で実行されるようにする。
ユーザが ubuntu 以外の場合は、`msbot-qiita-cron` の修正が必要。

```
sudo cp msbot-qiita-cron /etc/cron.d/
```

