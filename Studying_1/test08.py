import requests
import urllib.parse

keyword = "樊振东alc"
url = "https://api.m.jd.com/api"

params = {
    "appid": "search-pc-java",
    "client": "pc",
    "clientVersion": "1.0.0",
    "functionId": "pc_search_searchWare",
    "body": '{"enc":"utf-8","page":1,"s":1,"area":"1_72_55653_0"}',
    "keyword": urllib.parse.quote(keyword)
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://search.jd.com/",
}

resp = requests.get(url, params=params, headers=headers)
print(resp.text)

print("结果：", resp.text[:300])  # 打印前300字符看看有没有返回内容
