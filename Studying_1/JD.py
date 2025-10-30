import requests
import re
import json
import urllib.parse
import csv
import os


def search_jd_goods(keyword, page=1, limit=10):
    encoded_keyword = urllib.parse.quote(keyword)
    url = f"https://re.jd.com/s earch/getHotSaleGoods?keyword={encoded_keyword}&page={page}&cid3=1105&semword={encoded_keyword}&page_uuid=1a7ad341-ccb3-4803-818e-0b351fec0ebf&callback=jQuery17208969271872946369_1759893691368&_=1759893691409"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://search.jd.com/',
        'Accept': '*/*',
    }

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.encoding = 'utf-8'

        if resp.status_code != 200:
            print(f"请求失败，状态码：{resp.status_code}")
            return []

        match = re.search(r'jQuery\d+_\d+\((.*)\)', resp.text)
        if not match:
            print("无法解析JSONP响应")
            return []

        data = json.loads(match.group(1))
        goods_list = data.get('list', [])[:limit]

        results = []
        for goods in goods_list:
            name = goods.get('ad_title_text', '')
            price = goods.get('sku_price', '')
            sku_id = goods.get('sku_id', '')
            product_url = f"https://item.jd.com/{sku_id}.html" if sku_id else "链接不可用"
            results.append({"name": name, "price": price, "url": product_url})

        return results

    except Exception as e:
        print(f"发生错误：{e}")
        return []


def save_to_csv(keyword, goods_list):
    filename = "jd_goods.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["关键词", "商品名称", "价格", "链接"])

        for goods in goods_list:
            writer.writerow([keyword, goods["name"], goods["price"], goods["url"]])


def main():
    print("京东商品搜索工具（含CSV保存功能）")
    print("=" * 50)

    while True:
        keyword = input("\n请输入要搜索的商品关键词（输入'quit'退出程序）: ").strip()
        if keyword.lower() == 'quit':
            print("感谢使用，再见！")
            break
        if not keyword:
            print("关键词不能为空，请重新输入！")
            continue

        print("\n正在搜索，请稍候...")
        goods = search_jd_goods(keyword, limit=10)
        if not goods:
            print("未找到相关商品或请求失败。")
            continue

        print(f"搜索 '{keyword}' 的前 {len(goods)} 个商品信息：")
        for i, item in enumerate(goods, 1):
            print(f"{i}. {item['name']}")
            print(f"   价格: ￥{item['price']}")
            print(f"   链接: {item['url']}")
            print()

        save_to_csv(keyword, goods)
        print(f"✅ 数据已保存到 jd_goods.csv")


if __name__ == "__main__":
    main()
