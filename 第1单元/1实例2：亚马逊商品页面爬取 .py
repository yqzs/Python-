import requests
def getHTMLText(url):
    try:
        hd = {'user_agent':'Mozilla/5.0'}
        r = requests.get(url,headers = hd)
        r.raise_for_status() #如果不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "异常"

if __name__ == "__main__" :
    url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
    print(getHTMLText(url)[:1000])
