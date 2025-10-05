import requests
import json
from randcrack import RandCrack


URL = 'http://localhost:5000/check'
payload = {"attempt": 1}

rc = RandCrack()

r = requests.post(URL, json=payload)
rand_value = r.json()['ANSWER']
rc.submit(rand_value)

#print(r.headers['Set-Cookie'].split(';')[0].split('=')[1])
def create(r):
    return {'session': r.headers['Set-Cookie'].split(';')[0].split('=')[1]}

cookie = create(r)


for i in range(623):
    r = requests.post(URL, json=payload, cookies=cookie)
    #print(r.headers)
    rand_value = r.json()['ANSWER']
    rc.submit(rand_value)

for i in range(10):
    predict = rc.predict_randrange(0, 4294967295)
    #print(predict)
    payload = {"attempt": predict}
    r = requests.post(URL, json=payload, cookies=cookie)
    new_cookie = r.headers['Set-Cookie'].split(';')[0].split('=')[1]
    if new_cookie != cookie['session']:
        cookie['session'] = new_cookie
    #print(r.headers)
    print(r.json())

