# client functions for interacting with the ganbreeder api
import requests
import json

def login(username, password):
    def get_sid():
        url = 'https://ganbreeder.app/login'
        r = requests.get(url)
        r.raise_for_status()
        for c in r.cookies:
            if c.name == 'connect.sid': # find the right cookie
                print('Session ID: ' + str(c.value))
                return c.value

    def login_auth(sid, username, password):
        url = 'https://ganbreeder.app/login'
        headers = {
                'Content-Type': 'application/json',
                }
        cookies = {
                'connect.sid': sid
                }
        payload = {
                'email': username,
                'password': password
                }
        r = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(payload))
        if not r.ok:
            print('Authentication failed')
            r.raise_for_status()
        print('Authenticated')

    sid = get_sid()
    login_auth(sid, username, password)
    # print("Out login")
    return sid

def get_info(sid, key):
    # print("in get_info, key " + key)
    if sid == '':
        raise Exception('Cannot get info; session ID not defined. Be sure to login() first.')
    cookies = {
            'connect.sid': sid
            }
    url = 'http://ganbreeder.app/info?k='+key
    print(url)
    r = requests.get(url, cookies=cookies, timeout=5)
    r.raise_for_status()
    # print("out get_info")
    with open('jsonStore/'+key+'.json', 'w') as outfile:
        json.dump(r.json(), outfile)
    # json.dumps(r.json(),"jsonStore")
    return(r.json())

def get_info_batch(username, password, keys):
    l = list()
    sid = login(username, password)
    for key in keys:
        l.append(get_info(sid, key))
    # print("Out get_info_batch")
    return l
