import requests
from bs4 import BeautifulSoup
import pandas
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
url = "https://www.amazon.com/s?i=specialty-aps&bbn=16225013011&rh=n%3A%2116225013011%2Cn%3A2975481011&ref=nav_em__nav_desktop_sa_intl_horses_0_2_22_6"

request = requests.get(url,headers=headers)
soup = BeautifulSoup(request.text, 'lxml')

ranking = soup.select("")
#print(ranking)
name_list = []
price_list= []
discount_list = []
for el in ranking:
    name = el.select_one("")
    print(name)
    
    price = el.select_one("")
    if (name != None or price != None):
       name_list.append(name.text)
       price_list.append(price.text)
    

#print (name_list)
#print(price_list)
#data = pandas.DataFrame(name_list, columns=['Product Name'])
#print(data)
#data['Product Price'] = price_list
#print (data)

#data.to_csv("/Users/eugeneyoo/Desktop/DS Cocurric/ranking_chicken.csv")