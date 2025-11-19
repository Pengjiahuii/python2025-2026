import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import time
import re
from datetime import datetime
import matplotlib.font_manager as fm
from collections import Counter
import jieba
import jieba.analyse

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class XinhuaNewsAnalyzer:
    def __init__(self):
        self.base_url = "https://www.news.cn"
        self.news_data = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def crawl_news(self, keyword=None, pages=5):
        """
        爬取新华网新闻数据
        """
        print("开始爬取新华网新闻数据...")

        for page in range(1, pages + 1):
            print(f"正在爬取第 {page} 页...")

            try:
                response = requests.get(self.base_url, headers=self.headers, timeout=10)
                if response.status_code == 200:
                    self.parse_news_html(response.text)
                else:
                    print(f"请求失败，状态码: {response.status_code}")

                time.sleep(2)

            except Exception as e:
                print(f"爬取第 {page} 页时发生错误: {e}")
                continue

        print(f"爬取完成，共获取 {len(self.news_data)} 条新闻")

    def parse_news_html(self, html_content):

        title_pattern = r'<a href=\'([^\']+)\'[^>]*target=\'_blank\'>([^<]+)</a>'
        titles = re.findall(title_pattern, html_content)

        date_pattern = r'/(\d{8})/'

        for link, title in titles:
            if '/202' in link and '/c.html' in link:
                date_match = re.search(date_pattern, link)
                if date_match:
                    date_str = date_match.group(1)
                    try:
                        pub_date = datetime.strptime(date_str, '%Y%m%d')
                    except:
                        pub_date = datetime.now()
                else:
                    pub_date = datetime.now()

                if link.startswith('http'):
                    full_link = link
                else:
                    full_link = self.base_url + link if link.startswith('/') else self.base_url + '/' + link

                news_item = {
                    'title': title.strip(),
                    'link': full_link,
                    'pub_date': pub_date,
                    'content': '',
                    'source': '新华网'
                }

                self.news_data.append(news_item)

    def save_data(self, filename='D:/work/code/python/test/test/xinhua_news.csv'):
        if not self.news_data:
            print("没有数据可保存")
            return False

        df = pd.DataFrame(self.news_data)
        df['pub_date'] = df['pub_date'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"数据已保存到 {filename}")
        return True

    def load_data(self, filename='xinhua_news.csv'):
        try:
            df = pd.read_csv(filename, encoding='utf-8-sig')
            df['pub_date'] = pd.to_datetime(df['pub_date'])
            self.news_data = df.to_dict('records')
            print(f"从 {filename} 加载了 {len(self.news_data)} 条数据")
            return True
        except FileNotFoundError:
            print(f"文件 {filename} 不存在")
            return False
        except Exception as e:
            print(f"加载数据时发生错误: {e}")
            return False

    def clean_data(self, df):
        print("开始数据清洗...")

        initial_count = len(df)
        df = df.drop_duplicates(subset=['title', 'link'])
        print(f"去除重复数据: {initial_count} -> {len(df)}")

        df = df.dropna(subset=['title'])

        df['title_clean'] = df['title'].apply(lambda x: re.sub(r'[^\w\s]', '', str(x)))

        df['pub_date'] = pd.to_datetime(df['pub_date'])
        df['year'] = df['pub_date'].dt.year
        df['month'] = df['pub_date'].dt.month
        df['day'] = df['pub_date'].dt.day
        df['weekday'] = df['pub_date'].dt.weekday
        df['hour'] = df['pub_date'].dt.hour

        print("数据清洗完成")
        return df

    def extract_keywords(self, texts, top_k=20):
        """
        从文本中提取关键词
        """
        all_text = ' '.join([str(text) for text in texts if pd.notna(text)])
        keywords = jieba.analyse.extract_tags(all_text, topK=top_k, withWeight=True)
        return keywords

    def analyze_data(self):
        if not self.news_data:
            print("没有数据可分析")
            return None

        df = pd.DataFrame(self.news_data)
        df = self.clean_data(df)

        print("\n=== 数据分析结果 ===")

        print(f"总新闻数: {len(df)}")
        print(f"时间范围: {df['pub_date'].min()} 到 {df['pub_date'].max()}")

        daily_count = df.groupby(df['pub_date'].dt.date).size()
        print(f"日均新闻数: {daily_count.mean():.2f}")

        print("\n正在提取关键词...")
        keywords = self.extract_keywords(df['title_clean'])
        print("热门关键词:")
        for word, weight in keywords[:10]:
            print(f"  {word}: {weight:.3f}")

        return df

    def visualize_results(self, df):
        if df is None or len(df) == 0:
            print("没有数据可可视化")
            return

        # -----------------------------
        # 图 1：每日新闻数量 + 月度趋势 + 日分布箱线图
        # -----------------------------
        daily_count = df.groupby(df['pub_date'].dt.date).size()
        monthly_count = df.groupby('month').size()

        fig, axes = plt.subplots(2, 1, figsize=(14, 10))
        fig.suptitle("新华网新闻时间趋势分析", fontsize=16, fontweight='bold')

        # 上：每日新闻数量 + 趋势线
        axes[0].bar(daily_count.index, daily_count.values, alpha=0.4, label="每日新闻数")
        axes[0].plot(daily_count.index, daily_count.values, marker='o', linewidth=2, label="趋势线", color='orange')
        axes[0].set_xlabel("日期")
        axes[0].set_ylabel("新闻数量")
        axes[0].tick_params(axis='x', rotation=45)
        axes[0].grid(alpha=0.3)
        axes[0].legend()

        # 下：月度新闻堆叠 + 每日新闻箱线图
        axes[1].stackplot(monthly_count.index, monthly_count.values, alpha=0.5, colors=['skyblue'])
        axes_box = axes[1].twinx()
        axes_box.boxplot(daily_count.values, positions=[6.5], widths=0.5)
        axes[1].set_xticks(range(1, 13))
        axes[1].set_xlabel("月份")
        axes[1].set_ylabel("月度新闻量")
        axes_box.set_ylabel("每日新闻分布")
        axes[1].grid(alpha=0.3)

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.savefig("time_trend_analysis.png", dpi=300)
        plt.show()

        # -----------------------------
        # 图 2：星期分布 + 星期×小时热力图
        # -----------------------------
        df['weekday_name'] = df['weekday'].map({
            0: '周一', 1: '周二', 2: '周三', 3: '周四', 4: '周五', 5: '周六', 6: '周日'
        })
        weekday_count = df['weekday'].value_counts().sort_index()
        heatmap_data = df.pivot_table(index='weekday_name', columns='hour', aggfunc='size', fill_value=0)

        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        fig.suptitle("新华网新闻发布时间规律", fontsize=16, fontweight='bold')

        # 左：饼图
        axes[0].pie(weekday_count.values, labels=weekday_count.index.map({
            0: '周一', 1: '周二', 2: '周三', 3: '周四', 4: '周五', 5: '周六', 6: '周日'
        }), autopct='%1.1f%%', startangle=140, wedgeprops={"edgecolor": "white"})
        axes[0].set_title("新闻发布星期分布", fontsize=14)

        # 右：热力图
        im = axes[1].imshow(heatmap_data, aspect='auto', cmap='YlGnBu')
        axes[1].set_xticks(range(24))
        axes[1].set_yticks(range(7))
        axes[1].set_yticklabels(['周一', '周二', '周三', '周四', '周五', '周六', '周日'])
        axes[1].set_xlabel("小时")
        axes[1].set_ylabel("星期")
        axes[1].set_title("新闻发布时间热力图（星期 × 小时）", fontsize=14)
        plt.colorbar(im, ax=axes[1], label="新闻数量")

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.savefig("weekday_hour_analysis.png", dpi=300)
        plt.show()

        # -----------------------------
        # 图 3：关键词分析（词云 + 横向条形图）
        # -----------------------------
        try:
            from wordcloud import WordCloud
            keywords = self.extract_keywords(df['title_clean'], top_k=50)
            wc_dict = {word: weight for word, weight in keywords}

            fig, axes = plt.subplots(2, 1, figsize=(14, 12))
            fig.suptitle("新闻标题关键词分析", fontsize=16, fontweight='bold')

            # 上：词云
            wc = WordCloud(
                font_path="C:/Windows/Fonts/simhei.ttf",
                background_color="white",
                width=800,
                height=400
            ).generate_from_frequencies(wc_dict)
            axes[0].imshow(wc, interpolation='bilinear')
            axes[0].axis("off")
            axes[0].set_title("关键词词云", fontsize=14)

            # 下：横向条形图
            top15_words = [w for w, _ in keywords[:15]]
            top15_weights = [w for _, w in keywords[:15]]
            axes[1].barh(top15_words[::-1], top15_weights[::-1], color='steelblue')
            axes[1].set_xlabel("权重")
            axes[1].set_title("Top 15 关键词权重", fontsize=14)
            axes[1].grid(axis='x', alpha=0.3)

            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.savefig("keyword_analysis.png", dpi=300)
            plt.show()

        except ImportError:
            print("未安装 wordcloud，跳过词云图。")


def main():
    analyzer = XinhuaNewsAnalyzer()

    if not analyzer.load_data('xinhua_news.csv'):
        print("未找到现有数据文件，开始爬取数据...")
        pages = 3
        analyzer.crawl_news(pages=pages)
        analyzer.save_data('xinhua_news.csv')

    df = analyzer.analyze_data()

    if df is not None:
        analyzer.visualize_results(df)

        print("\n" + "=" * 50)
        print("新华网新闻分析报告")
        print("=" * 50)
        print(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"分析数据量: {len(df)} 条新闻")
        print(f"时间跨度: {df['pub_date'].min().strftime('%Y-%m-%d')} 至 {df['pub_date'].max().strftime('%Y-%m-%d')}")

        weekday_news = len(df[df['weekday'] < 5])
        weekend_news = len(df[df['weekday'] >= 5])
        print(f"工作日新闻数量: {weekday_news}")
        print(f"周末新闻数量: {weekend_news}")
        print(f"工作日/周末比例: {weekday_news / weekend_news:.2f}:1")

        keywords = analyzer.extract_keywords(df['title_clean'], top_k=20)
        print("\n关键词分析 (前20):")
        for i, (word, weight) in enumerate(keywords, 1):
            print(f"{i:2d}. {word:<10} {weight:.4f}")


if __name__ == "__main__":
    main()