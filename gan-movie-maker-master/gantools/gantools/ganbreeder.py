# client functions for interacting with the ganbreeder api
import requests
import json
import numpy as np
import biggan

def login(username, password):
    def get_sid():
        url = 'https://artbreeder.com/login'
        r = requests.get(url)
        r.raise_for_status()
        for c in r.cookies:
            if c.name == 'connect.sid': # find the right cookie
                print('Session ID: ' + str(c.value))
                return c.value

    def login_auth(sid, username, password):
        url = 'https://artbreeder.com/login'
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
    return sid

def parse_info_dict(info):
    keyframe = dict()
    keyframe['truncation'] = np.float(info['truncation'])
    keyframe['latent'] = np.asarray(info['latent'])
    #keyframe['latent'] = np.asarray(info['wlatent_idxs'])
    classes = info['classes']
    #classes = info['base64_arrays']
    keyframe['label'] = np.zeros(1000)# length of label ("classes") vector: 1000
    for c in info['classes']:
    #for c in info['base64_arrays']:
        # artbreeder class entries look like [index, value] where index < 1000
        keyframe['label'][c[0]] = c[1]
    return keyframe

def get_info(sid, key):
    if sid == '':
        raise Exception('Cannot get info; session ID not defined. Be sure to login() first.')
    cookies = {
            'connect.sid': sid
            }
    #key = "215d3c08abb5280283b9afc6";
    #key = "7968340a72eabab735d04dba";
    print("la");
    print(key[0])
    key = key.replace("'", "")
    print(key);
    print("la");
    r = requests.get('http://artbreeder.com/info?k='+str(key), cookies=cookies)
    #r = requests.get('http://example.com')
    # print("la");
    # print(r.json());
    # print("la");
    r.raise_for_status()
    return parse_info_dict(r.json())

def get_info_batch(username, password, keys):
    l = list()
    # print("la");
    # print(username);
    # print("la");
    sid = login(username, password)
    x = []
    x = x + keys[0].split()
    # print(x)
    # print(x[0])
    for key in x:
        # print("key")
        # print(key)
        l.append(get_info(sid, key))
    return l
