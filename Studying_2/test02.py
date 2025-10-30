import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_xinhua_latest():
    url = "https://www.news.cn/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        print("📢 新华网新闻提取结果")
        print("=" * 60)

        # 定义关键词匹配（因为新版页面 class 名会变化）
        sections = {
            "焦点新闻": ["focus-newsMedia", "focus-news", "headlines", "photo-news"],
            "置顶新闻": ["focus-newsMedia-top", "top-news", "headline"],
            "新华系列报刊": ["channel newspapers", "newspaper", "bkdy"]
        }

        all_news = []

        for section_name, possible_classes in sections.items():
            print(f"\n🎯 {section_name}:")
            found = False
            for cls in possible_classes:
                container = soup.find('div', class_=cls) or soup.find('section', class_=cls)
                if container:
                    found = True
                    links = container.find_all('a', href=True)
                    count = 0
                    for link in links:
                        title = link.get_text(strip=True)
                        href = link.get('href')
                        if title and len(title) > 4:
                            full_url = urljoin(url, href)
                            count += 1
                            print(f"{count}. {title}")
                            print(f"   链接: {full_url}")
                            all_news.append((title, full_url))
                    if count == 0:
                        print("   暂无可用新闻链接。")
                    break
            if not found:
                print("   未找到该分类的新闻区块。")

        print(f"\n✅ 共提取到 {len(all_news)} 条新闻。")
        return all_news

    except requests.exceptions.RequestException as e:
        print(f"❌ 网络请求失败: {e}")
        return []
    except Exception as e:
        print(f"⚠️ 解析错误: {e}")
        return []


if __name__ == "__main__":
    news_list = fetch_xinhua_latest()
