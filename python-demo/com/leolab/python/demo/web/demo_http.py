import urllib.request as ur
import json

url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2114972825&containerid=1076032114972825&since_id=4298781241907056'
req = ur.Request(url)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# url = 'http://m.baidu.com'
conn = ur.urlopen(req)
# print(conn.status)
# print(conn.getheader('Content-Type'))
# for key, value in conn.getheaders():
#     print(key, " : ", value)
data = conn.read()
print(data)
json_obj = json.loads(data)
cards = json_obj['data']['cards']
print(json_obj['data']['cards'])
for card in cards:
    if '9'.__eq__(str(card['card_type'])):
        print(card['mblog']['text'])

