from bs4 import BeautifulSoup
import requests
import  re
r = requests.get('https://python123.io/ws/demo.html')
soup = BeautifulSoup(r.text,'html.parser')
'''
for link in soup.find_all('a'):  #找出a标签包含的链接
	print(link.get('href'))
for tag in soup.find_all(True):    
	print(tag.name)
for tag in soup.find_all(re.compile('b')):
	print(tag.name)
print(soup.find_all(id = re.compile('link')))
'''
print(soup.find_all(string = re.compile('Python')))  #查找字符串
r = requests.get('http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html')
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())