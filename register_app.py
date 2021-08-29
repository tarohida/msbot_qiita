from mastodon import Mastodon

url = 'https://qiitadon.com'
app_name = 't-bot'
cred_file_path = './account_info/cred.txt'
auth_file_path = './account_info/auth.txt'
login_mail_address = ''
login_password = ''

Mastodon.create_app(
    app_name,
    api_base_url=url,
    to_file=cred_file_path
)
mastodon = Mastodon(
    client_id=cred_file_path,
    api_base_url=url
)
mastodon.log_in(
    login_mail_address,
    login_password,
    to_file=auth_file_path
)
