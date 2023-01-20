import requests
from bs4 import BeautifulSoup


#오늘의 환율 스크래이핑 하기

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=2&acq=%ED%99%98%EC%9C%A8&qdt=0&ie=utf8&query=%ED%99%98%EC%9C%A8"
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

rate = soup.select("#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.dw > strong")
print("One U.S. Dollar is equal to",rate[0].text,"Korean Won today.")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
url2 = "https://www.google.com/search?q=temperature&rlz=1C5CHFA_enKR1017KR1017&oq=temperature&aqs=chrome..69i57j35i39j0i67j0i67i457j0i402j0i67l3j0i512l2.1833j0j7&sourceid=chrome&ie=UTF-8"
res2 = requests.get(url2, headers = headers)
soup2 = BeautifulSoup(res2.text, "lxml")
temperature = soup2.select('#wob_tm')
print ("Today's temperature in your area is",temperature[0].text,"degrees celcius.")
