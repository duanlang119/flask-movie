import requests

# r = requests.get('http://127.0.0.1:5000/login', auth=('magigo','123456'))
# print(r.text)


payload = {'token': 'bWFnaWdvOjAuOTE2MzAzODA3OTk0Njg2MjoxNTc4MTQxNzk4LjAzNDU2NzY='}
r = requests.get('http://127.0.0.1:5000/test1', params=payload)
print (r.text)