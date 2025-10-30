import requests
from bs4 import BeautifulSoup

url = "https://www.runoob.com/python3/python3-tutorial.html"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

# 提取左侧导航栏
nav_div = soup.find("div", id="leftcolumn")
links = nav_div.find_all("a")

print("【左侧导航栏URL与标题】")
for link in links:
    title = link.get_text(strip=True)
    href = link.get("href")
    print(f"{title} -> {href}")
