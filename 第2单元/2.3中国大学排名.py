import requests
from bs4 import  BeautifulSoup
import bs4
import re
def getHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print("异常")
    return  r.text

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string, tds[1].string, tds[2].string])


def printUnivList(ulist ,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format('排名','大学','总分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHtmlText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)  #20 universities
main()