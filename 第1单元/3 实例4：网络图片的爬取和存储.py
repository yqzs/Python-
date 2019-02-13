import requests
import os
url = 'https://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
root = "C://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exist(root):    #创建路径
        os.mkdir(root)
    if not os.path.exists(path):   #检查文件是否存在
        r = requests.get(url)
        with open(path,'wb') as f:    #覆盖写模式打开
            f.write(r.content)
            f.close()
            print('保存成功')
    else:
        print('文件已存在')
except:
    print("爬取失败")

