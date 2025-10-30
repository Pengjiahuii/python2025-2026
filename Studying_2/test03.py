from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, requests

keyword = "樊振东"
save_dir = r"D:\PycharmProjects\python2025——2026\Studying_2"
os.makedirs(save_dir, exist_ok=True)

driver = webdriver.Chrome()  # 确保chromedriver已安装
driver.get("https://image.baidu.com/")

try:
    # 等待搜索框加载完成
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@class="s_ipt"]'))
    )
    search_box.send_keys(keyword)

    # 点击搜索按钮
    search_button = driver.find_element(By.XPATH, '//span[@class="s_search"]')
    search_button.click()

    time.sleep(3)  # 等待图片加载

    images = driver.find_elements(By.TAG_NAME, "img")
    count = 0
    for img in images[:20]:
        src = img.get_attribute("src")
        if src and "http" in src:
            try:
                img_data = requests.get(src).content
                with open(os.path.join(save_dir, f"{keyword}_{count+1}.jpg"), "wb") as f:
                    f.write(img_data)
                count += 1
                print(f"✅ 保存图片 {count}")
            except Exception as e:
                print(f"⚠️ 下载失败: {e}")

finally:
    driver.quit()

print(f"🎉 共保存 {count} 张图片")
