import requests
from bs4 import BeautifulSoup
import pandas
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
url = "https://www.rankingdak.com/promotion/exhibit/list?NaPm=ct%3Dla0ofrhm%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3Da2ab61cbd79800946ef7ac81b0a4d8d13543c1fc"

request = requests.get(url,headers=headers)
soup = BeautifulSoup(request.text, 'lxml')

ranking = soup.select("#special-div1 > ul > li")
#print(ranking)
name_list = []
price_list= []
discount_list = []
for el in ranking:
    name = el.select_one("p.tit > a")
    #print(name)
    price = el.select_one("span.price > em")
    if (name != None and price != None):
        name_list.append(name.text)
        price_list.append(price.text)
    

#print (name_list)
#print(price_list)
data = pandas.DataFrame(name_list, columns=['Chicken Name'])
print(data)
data['Chicken Price'] = price_list
print (data)

data.to_csv("/Users/eugeneyoo/Desktop/DS Cocurric/ranking_chicken.csv")