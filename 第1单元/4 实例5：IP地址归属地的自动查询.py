import requests
def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status() #如果不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r
    except:
        return "异常"

if __name__ == "__main__" :
    url1 = 'http://www.ip138.com/ips138.asp?ip=202.204.80.112&action=2'
    url2 = '&action=2'
    ip = input('请输入ip地址')
    url = url1 + ip + url2
    print(getHTML(url).text[:])
