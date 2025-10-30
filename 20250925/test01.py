with open('example.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(f'文件共有{len(lines)}行')
    for l in lines:
        print(l.strip())