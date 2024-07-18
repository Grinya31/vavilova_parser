import requests
from bs4 import BeautifulSoup
import lxml


url = "https://shop.kerama-marazzi.ru/catalog/santekhnika-kerama-marazzi/"

response=requests.get(url)


soup=BeautifulSoup(response.text,'lxml')

glav_name=soup.find_all('div',class_="col-md-4 col-sm-6 text-center")

for b in glav_name:
    name=b.find('span',class_="catalog-title")
    c=[i for i in name]
    print(c[0])

#data=soup.find('div', class_='col-xl-3 col-md-4 col-sm-6 mt-3')
#data=soup.find_all('div', class_='col-xl-3 col-md-4 col-sm-6 mt-3')
#print(data)
#for i in data:

    #name=i.find('a', class_='title').text.replace('\n','')
    #price=i.find('div', class_="current").text.replace(' ','')
    #url_image="https://shop.kerama-marazzi.ru/"+i.find('a',class_='img-wrap').get('href')

    #print(name + '\n'+ price + '\n' + url_image)