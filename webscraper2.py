import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
request = requests.get(url)
soup = BeautifulSoup(request.text, 'lxml')

rank = soup.select("#old_content > table > tbody > tr")

for tr in rank:
    movie= tr.select_one("td.title > div > a")
    if movie != None:
        print (movie.text)

