import requests
from getpass import getpasss

def pasteAsGuest():
    paste_url = 'https://pastebin.com/api/api_post.php'
    user_data = {'api_dev_key': dev_key,
                'api_option': 'paste',
                'api_paste_code': paste_code,
                'api_paste_name': paste_name
                }
    paste = requests.post(paste_url, data = user_data)
    print(f'This is your required paste URL: {paste.text}')

def pasteAsUser():
    paste_url = 'https://pastebin.com/api/api_post.php'
    user_data = {'api_dev_key': dev_key,
                'api_user_key': temp.text,
                'api_option': 'paste',
                'api_paste_code': paste_code,
                'api_paste_name': paste_name
                }
    paste = requests.post(paste_url, data = user_data)
    print(f'This is your required paste URL: {paste.text}')



dev_key = ''  #paste your unique API developer key you get after signing in to https://pastebin.com
paste_code = input('What do you want to paste? ')
paste_name = input('Paste Name: ')
if not paste_name:
    paste_name = 'Untitled'
user_name = input('User Name: ')
user_password = getpass()

login_url = 'https://pastebin.com/api/api_login.php'
create_user_key = {'api_dev_key': dev_key,
                    'api_user_name': user_name,
                    'api_user_password': user_password
                    }
temp = requests.post(login_url, data = create_user_key)

if 'Bad API request' in temp.text:
    print('Invalid password, pasting as a guest')
    pasteAsGuest()
else:
    pasteAsUser()
