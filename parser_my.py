import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
 

def get_card_url():
    for count in range(1,3):
        url=f'https://shop.kerama-marazzi.ru/catalog/santekhnika-kerama-marazzi/?PAGEN_1={count}'
        response=requests.get(url,headers=headers)
        soup=BeautifulSoup(response.text,'lxml')
        cat_name=soup.find_all('div',class_="col-md-4 col-sm-6 text-center")
        for i in cat_name:
            name ="https://shop.kerama-marazzi.ru"+i.find('a').get('href')
            yield name

def array():
    for card_url in get_card_url():
        response=requests.get(card_url,headers=headers)
        soup=BeautifulSoup(response.text,'lxml')
        tovars=soup.find_all('div',class_="col-xl-3 col-md-4 col-sm-6 mt-3")
        for i in tovars:
            name=i.find('a', class_='title').text
            link="https://shop.kerama-marazzi.ru"+i.find('a',class_='title').get('href')
            img_link="https://shop.kerama-marazzi.ru"+i.find('a').get('href')
            yield name,link,img_link,
    
            
        

        


#data=soup.find('div', class_='col-xl-3 col-md-4 col-sm-6 mt-3')
#data=soup.find_all('div', class_='col-xl-3 col-md-4 col-sm-6 mt-3')
#print(data)
#for i in data:

    #name=i.find('a', class_='title').text.replace('\n','')
    #price=i.find('div', class_="current").text.replace(' ','')
    #url_image="https://shop.kerama-marazzi.ru/"+i.find('a',class_='img-wrap').get('href')

    #print(name + '\n'+ price + '\n' + url_image)