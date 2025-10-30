import requests
from bs4 import BeautifulSoup

def scrape_runoob():
    url = "https://www.runoob.com/python3/python3-tutorial.html"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, "html.parser")

    # 获取目录列表
    links = soup.select(".left-column a")
    if not links:
        print("没有找到匹配内容，请检查选择器。")
        return

    with open("runoob_result.txt", "w", encoding="utf-8") as f:
        for link in links:
            title = link.get_text(strip=True)
            href = link.get("href", "")
            f.write(f"{title} — {href}\n")

    print("静态抓取完成，结果保存到 runoob_result.txt")

if __name__ == "__main__":
    scrape_runoob()
