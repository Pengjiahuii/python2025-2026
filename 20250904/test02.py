import random

# 生成 1 到 100 之间的随机整数
secret = random.randint(1, 100)

print("🎲 猜数字游戏开始！（范围 1~100）")

while True:
    guess = int(input("请输入你的猜测："))

    if guess > secret:
        print("太大了！再试一次～")
    elif guess < secret:
        print("太小了！再试一次～")
    else:
        print("恭喜你，猜对了！答案就是", secret)
        break
