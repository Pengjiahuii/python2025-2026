import requests
import re
import json
import urllib.parse


def search_jd_goods(keyword, page=1):

    encoded_keyword = urllib.parse.quote(keyword)

    url = f"https://re.jd.com/search/getHotSaleGoods?keyword={encoded_keyword}&page={page}&cid3=1105&semword={encoded_keyword}&page_uuid=1a7ad341-ccb3-4803-818e-0b351fec0ebf&callback=jQuery17208969271872946369_1759893691368&_=1759893691409"

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'Referer': 'https://search.jd.com/',
        'Accept': '*/*',
    }

    try:
        resp = requests.get(url, headers=header, timeout=10)
        resp.encoding = 'utf-8'

        if resp.status_code == 200:
            text = resp.text
            match = re.search(r'jQuery\d+_\d+\((.*)\)', text)
            if match:
                json_str = match.group(1)
                data = json.loads(json_str)

                goods_list = data.get('list', [])

                if goods_list:
                    print(f"搜索 '{keyword}' 的商品信息（第{page}页）：")
                    print("=" * 80)

                    for index, goods in enumerate(goods_list, 1):
                        # 获取商品介绍（名称）
                        name = goods.get('ad_title_text', '')
                        # 获取价格
                        price = goods.get('sku_price', '')
                        # 获取商品ID，用于构建商品链接
                        sku_id = goods.get('sku_id', '')

                        # 构建商品链接
                        product_url = f"https://item.jd.com/{sku_id}.html" if sku_id else "链接不可用"

                        print(f"{index}. {name}")
                        print(f"   价格: ￥{price}")
                        print(f"   链接: {product_url}")
                        print()

                    print(f"共找到 {len(goods_list)} 个商品")
                    return len(goods_list)
                else:
                    print(f"未找到与 '{keyword}' 相关的商品数据")
                    return 0
            else:
                print("无法解析JSONP响应")
                return 0

        else:
            print(f"请求失败，状态码：{resp.status_code}")
            return 0

    except Exception as e:
        print(f"发生错误：{e}")
        return 0


def main():
    print("京东商品搜索工具")
    print("=" * 50)

    while True:
        # 获取用户输入
        keyword = input("\n请输入要搜索的商品关键词（输入'quit'退出程序）: ").strip()

        if keyword.lower() == 'quit':
            print("感谢使用，再见！")
            break

        if not keyword:
            print("关键词不能为空，请重新输入！")
            continue

        # 询问页码
        try:
            page = input("请输入页码（默认为1）: ").strip()
            page = int(page) if page else 1
            if page < 1:
                page = 1
        except ValueError:
            print("页码输入无效，使用默认页码1")
            page = 1

        print("\n正在搜索，请稍候...")
        result_count = search_jd_goods(keyword, page)

        # 如果找到商品，询问是否继续搜索下一页
        if result_count > 0:
            next_page = input(f"\n是否搜索下一页？(y/n, 默认为n): ").strip().lower()
            if next_page == 'y' or next_page == 'yes':
                search_jd_goods(keyword, page + 1)


if __name__ == "__main__":
    main()