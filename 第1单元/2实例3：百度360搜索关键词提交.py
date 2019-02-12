import requests
def getHTMLText(url,kv):
    try:
        hd = {'user_agent':'Mozilla/5.0'}
        r = requests.get(url,headers = hd,params = kv)
        r.raise_for_status() #如果不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "异常"

if __name__ == "__main__" :
    keyword = input('请输入搜索关键词')
    a = input('使用百度请按1，使用360搜索请按2')
    if a == '1':
        kv = {'wd=':keyword}
        url = "https://www.baidu.com/s"
    if a ==  '2':
        kv ={'q':keyword}
        url = "https://www.so.com/s"
  
    print(getHTMLText(url,kv)[:])
