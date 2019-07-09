import requests
from bs4 import BeautifulSoup

# 1. url 설정
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
# 2. 요청 보내기
response = requests.get(url).text
# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(response, 'html.parser')
# 4. 원하는 내용 선택자로 뽑아내기
# table = soup.select_one('body > div > table > tbody')
# print(table)
table = soup.select('body > div > table > tbody > tr')
# print(len(table))
# print(type(table))
for tr in table:
    print(tr.select_one('td.tit').text)

for tr in table:
    print(tr.select_one('td.sale').text)

# body > div > table > tbody > tr:nth-child(1) > td.tit
# body > div > table > tbody > tr:nth-child(1) > td.sale