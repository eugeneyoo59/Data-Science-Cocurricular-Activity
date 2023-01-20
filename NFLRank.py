import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
url = "https://www.teamrankings.com/nfl/"

request = requests.get(url,headers=headers)
soup = BeautifulSoup(request.text, 'lxml')
#print (soup)
ranking = soup.select("#league-overview-table > tbody > tr")
#print(ranking)
for tr in ranking:
     element = tr.select_one("#league-overview-table > tbody > tr > td.nowrap > div > div.table-team-logo-text > a")
     if (element != None):
        print (element.text)