import urllib.request, urllib.parse, urllib.error
from beautiful import BeautifulSoup

url=input("Enter the url")
if len(url)<1:
   url =' http://py4e-data.dr-chuck.net/known_by_Flynn.html'
try:
   link_pos=int(input("Ener the link position:"))
   repeat=int(input("Enter the number of repetaion:"))
except ValueError:
       print("Enter the integer value and try again.")
       quit()
def finding_links(link):
    html=urllib.request.urlopen(link).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    return tags
name_list=list()
for count in range(repeat):
    tags=finding_links(url)
    recursion_link=tags[link_pos-1].get('href',None)
    name_list.append(tags[link_pos-1].contents[0])
    url=recursion_link
    print(name_list)
    print(name_list[-1])
