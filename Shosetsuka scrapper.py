import time
from urllib import request
from bs4 import BeautifulSoup

num_parts = 9000 
nam = input("enter the name of the novel ")



namend = (".txt")
fullnam = nam + namend
sityy = input("enter a syosetu site for ex http://ncode.syosetu.com/n0865em/ and don't forget to add a / at the end of n0865em  ")
res = request.urlopen(sityy)
soup = BeautifulSoup(res, "html.parser")
num_parts = (-0) 
for chapters in soup.find_all("dl"):
    num_parts = num_parts + 1
 
with open(fullnam, "w", encoding="utf-8") as f:
    for part in range(1, num_parts):

        url = sityy + "{:d}/".format(part)

        res = request.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")

    
        honbun = soup.select_one("#novel_honbun").text
        honbun += "\n"  

        f.write(honbun)

        print("part {:d} downloaded".format(part))  

        time.sleep(1)  
print("done, enjoy")