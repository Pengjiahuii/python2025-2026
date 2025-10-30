with open('source.txt', 'r', encoding='utf-8') as src:
    with open('copy.txt', 'w', encoding='utf-8') as cpy:
        content = src.read()
        content = content.replace('Java', 'Python').replace('java', 'python')
        content = content.replace('第一行', 'Line1').replace('第二行', 'Line2').replace('第三行', 'Line3')
        cpy.write(content)