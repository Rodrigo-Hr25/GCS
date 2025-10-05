import random, time
import requests
from randcrack import RandCrack

random.seed(time.time())

rc = RandCrack()
s = requests.Session()

for i in range(624):
    data = {"attempt": "191919199"}
    url = "http://localhost:5000/generate"
    response = s.get(url)
    url = "http://localhost:5000/check"
    response = s.post(url,json=data)
    rc.submit(int(response.json()['ANSWER']))
	# Could be filled with random.randint(0,4294967294) or random.randrange(0,4294967294)

for i in range(10):
    data = {"attempt": rc.predict_randrange(0, 4294967295)}
    url = "http://localhost:5000/generate"
    response = s.get(url)
    url = "http://localhost:5000/check"
    response = s.post(url,json=data)
    print("Result: {}".format(response.json()))