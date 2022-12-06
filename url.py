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











#You can replace the content of a text or file with sub from the regex module (re):

def replace_content(dict_replace, target):
    """Based on dict, replaces key with the value on the target."""

    for check, replacer in list(dict_replace.items()):
        target = sub(check, replacer, target)

    return target
#Or just with str.replace which does not need from re import sub:

def replace_content(dict_replace, target):
    """Based on dict, replaces key with the value on the target."""

    for check, replacer in list(dict_replace.items()):
        target = target.replace(check, replacer)

    return target
#Here's the full implementation:

from re import sub
from os.path import abspath, realpath, join, dirname

file = abspath(join(dirname(__file__), 'num.txt'))
file_open = open(file, 'r')
file_read = file_open.read()
file_open.close()

new_file = abspath(join(dirname(__file__), 'number.txt'))
new_file_open = open(new_file, 'w')


def replace_content(dict_replace, target):
    """Based on dict, replaces key with the value on the target."""

    for check, replacer in list(dict_replace.items()):
        target = sub(check, replacer, target)
        # target = target.replace(check, replacer)

    return target


# check : replacer
dict_replace = {
    'ipsum': 'XXXXXXX',
    'amet,': '***********',
    'dolor': '$$$$$'
}
dict_replace = {
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
new_content = replace_content(dict_replace, file_read)
new_file_open.write(new_content)
new_file_open.close()

# Test
print(file_read)
# Lorem ipsum dolor sit amet, lorem ipsum dolor sit amet

print(new_content)
# Lorem XXXXXXX $$$$$ sit ******
with open('number.txt','r') as number:
  for i in number:
     selectnode(mode='sms', num=str(i))
     selectnode(mode='call', num=str(i))
