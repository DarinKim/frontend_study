# =========================================================
# pymongo 연습01: DB 연결하기 & 데이터 생성하기(Create)
# =========================================================
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# MontoDB에 insert 하기

# 'users'라는 collection 데이터를 생성합니다.
db.users.insert_one({'name': '덤블도어', 'age': 116})
db.users.insert_one({'name': '맥고나걸', 'age': 85})
db.users.insert_one({'name': '스네이프', 'age': 60})
db.users.insert_one({'name': '해리', 'age': 40})
db.users.insert_one({'name': '허마이오니', 'age': 40})
db.users.insert_one({'name': '론', 'age': 40})

# =========================================================
# pymongo 연습 02-1: DB 저장된 값을 조회하기 (Read)
# =========================================================
# from pymongo import MongoClient
#
# client = MongoClient('localhost', 270717)
# db = client.dbsparta

# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))

print(all_users[0])
print(all_users[0]['name'])

for user in all_users:
    print(user)

# =========================================================
# pymongo 연습 02-2: DB 저장된 특정값을 조회하기 (Read)
# =========================================================
# MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age':40}))

for user in same_ages:
    print(user)

user = db.users.find_one({'name': '덤블도어'})
print(user)

# 그 중 특정 키 값을 빼고 보기
user = db.users.find_one({'name': '덤블도어'}, {'_id': False})
print(user)

# =========================================================
# pymongo 연습 03: 값 업데이트하기 (Update)
# =========================================================
db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})
user = db.users.find_one({'name': '덤블도어'})
print(user)

# =========================================================
# pymongo 연습 04: 삭제하기 (Delete)
# =========================================================
db.users.delete_one({'name': '론'})

user = db.users.find_one({'name': '론'})
print(user)