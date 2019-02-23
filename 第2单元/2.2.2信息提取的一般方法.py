from bs4 import BeautifulSoup
import requests
import  re
r = requests.get('https://python123.io/ws/demo.html')
soup = BeautifulSoup(r.text,'html.parser')
'''
for link in soup.find_all('a'):
	print(link.get('href'))
for tag in soup.find_all(True):
	print(tag.name)
for tag in soup.find_all(re.compile('b')):
	print(tag.name)
	'''
print(soup.find_all(id = re.compile('link')))