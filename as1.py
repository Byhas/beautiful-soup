from urllib import request
from beautiful import BeautifulSoup
html=request.urlopen('http://python-data.dr-chuck.net/comments_1310148.html').read()
soup = BeautifulSoup(html)
tags=soup('span')
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)
