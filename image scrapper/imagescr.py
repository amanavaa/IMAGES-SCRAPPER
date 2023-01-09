import requests
from bs4 import BeautifulSoup

url="https://www.pinterest.com/inspirationfeed/motivational-picture-quotes"

res = requests.get(url)

soup= BeautifulSoup(res.content, "html.parser")

# print(soup.title.text)
# here we access the div class where image parent 
parentimg = soup.find_all('div' , class_="Pj7 sLG XiG ho- m1e" )
# THERE IS TWO WAYS FOR ACCESS A IMAGE 
    #    1 WAY
# print(parentimg)
# here we access all the img tag form the div class
# imasrc = [x.find('img') for x in parentimg]
# here we access all src from img tag
# srclist = [ img['src'] for img in imasrc]
# print(srclist)


    # 2 WAYS
imgtag=[]
for x in parentimg[1:6]:
    imgtag.append(x.find('img'))
    # print(imgtag)
srclist =[img['src'] for img in imgtag] 
print(srclist)

# this related for download all the scrapped images
i=1
for src in srclist:
   res1 = requests.get(src)
   f =open(f'img-{i}.jpg' , 'wb')
   f.write(res1.content)
   f.close()
   i+=1



