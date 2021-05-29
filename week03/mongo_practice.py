import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        # a의 text를 찍어본다.
        rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
        title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
        star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
        # print(rank, title, star)
        doc = {
            'rank' : rank,
            'title' : title,
            'star' : star   # DB에는 숫자처럼 생긴 문자열 형태로 저장됩니다.
        }
        db.movies.insert_one(doc)

# find, update 연습하기
# 1) 영화 제목 '월-E'의 평점 가져오기
target_movie = db.movies.find_one({'title':'월-E'})
print(target_movie['star'])
# 2) '월-E'의 평점과 같은 평점의 영화 제목 가져오기
target_star = target_movie['star']
movies = list(db.movies.find({'star': target_star}))
for movie in movies:
    print(movie['title'])
# 3) '월-E'의 평점과 같은 영화 제목들의 평점을 0으로 만들기
db.movies.update_many({'star': target_star}, {'$set': {'star': '0'}})      # 'star': 0 으로 했더니 못알아먹음,, '0'으로 해야 동작