import requests
from bs4 import BeautifulSoup
 
RANK = 100 ## 멜론 차트 순위가 1 ~ 100위까지 있음

# 기본적으로 http의 header에는 여러 헤더 존재하는데, User-Agent 헤더는 현재 사용자가 어떤 클라이언트 이용해 요청 보냈는지 서버에 알려줌
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}       
req = requests.get('https://www.melon.com/chart/week/index.htm', headers = header)      # 헤더 같이 안보내면 가끔 튕겨나감
html = req.text                                                                         # 받아온 데이터를 text로 저장
parse = BeautifulSoup(html, 'html.parser')                                              # BeautifulSoup 라이브러리로 html로 파싱

titles = parse.find_all("div", {"class": "ellipsis rank01"})                            # 제목 가장 가까운 class 옆 이름
singers = parse.find_all("div", {"class": "ellipsis rank02"})                           # 가수 가장 가까운 class 옆 이름
albums = parse.find_all("div",{"class": "ellipsis rank03"})                             # 앨범 가장 가까운 class 옆 이름

title = []
singer = []
album = []

for t in titles:
    title.append(t.find('a').text)

for s in singers:
    singer.append(s.find('span', {"class": "checkEllipsis"}).text)

for a in albums:
    album.append(a.find('a').text)

# 최종
for i in range(RANK):
    print('%3d위: %s [ %s ] - %s'%(i+1, title[i], album[i], singer[i]))
