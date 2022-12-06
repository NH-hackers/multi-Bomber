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


import re

def word_replace(text, replace_dict):
    rc = re.compile(r"[A-Za-z_]\w*")

def translate(match):
    word = match.group(0).lower()
    print(word)
    return replace_dict.get(word, word)

#return rc.sub(translate, text)

old_text = open('num.txt').read()

replace_dict = {
"9798092707" : "",
"6203801709" : "",
"9835023651" : "",
"9142372789" : "",
"7367027640" : "",
"6299165979" : "",
"8102892250" : "",
"9031190441" : "",
"7759927677" : ""
}




output = word_replace(old_text, replace_dict)
f = open("number.txt", 'w')                   #what file you want to write to
#f.write(output)                              #write to the file
print(output)
with open('number.txt','r') as number:
  for i in number:
     selectnode(mode='sms', num=str(i))
     selectnode(mode='call', num=str(i))
