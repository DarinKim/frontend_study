# 자료형: 숫자, 문자
name = 'Harry'
print(name)

num = 12
print(num)

name = 13
print(name)

number_status = True
print(number_status)

# 자료형: list, Dictionary
a_list = []
a_list.append(1)
print(a_list)

a_list.append([2, 3])
print(a_list)
print(a_list[1][0])

a_dict = {}
wizard = {'name': 'Harry Potter', 'age': 40}
print(wizard)

wizard['height'] = 173
print(wizard)
print(wizard['name'])

# 자료형: list와 dictionary의 조합
wizards = [{'name' : 'Harry Potter', 'age': 40}, {'name' : 'Ron Weasley', 'age' : 40}]
print(wizards)
print(wizards[0]['name'])
print(wizards[1]['name'])

new_wizard = {'name': 'Albus Potter', 'age':14}
wizards.append(new_wizard)
print(wizards)
print(wizards[2]['name'])

# 함수
def sum_all(a,b,c):
    return a+b+c
def mul(a, b):
    return a*b

result = sum_all(1, 2, 3) + mul(10, 10)
print(result)

# 함수 + 조건문, 반복문
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = is_even(20)
print(result)

def is_adult(age):
    if age >= 20:
        print('성인입니다')
    else:
        print('성인이 아니에요')

is_adult(30)

def check_generation(age):
    if age > 120:
        print('와 19세기에 태어나셨군요!')
    elif age >= 80:
        print('80세 이상! 인생은 여든부터!')
    else:
        print('젊으시군요! 장래희망이 뭔가요?')

my_age = 55
check_generation(my_age)

fruits = ['사과', '배', '감', '귤']
for fruit in fruits:
    print(fruit)

fruits += ['배', '수박', '딸기', '사과', '배', '수박']
print(fruits)

count = 0
for fruit in fruits:
    if fruit == '사과':
            count += 1
print(count)

print('====== count_fruits 함수 ======')
def count_fruits(name):
    count = 0
    for fruit in fruits:
        if fruit == name:
            count += 1
    return count

subak_count = count_fruits('수박')
print(subak_count)

gam_count = count_fruits('감')
print(gam_count)

wizards = [
    {'name' : '해리', 'age':40},
    {'name':'허마이오니', 'age':40},
    {'name':'론', 'age':41},
]

for wizard in wizards:
    print(wizard['name'], wizard['age'])

print('===== 교수님 나이 찾기 ====')
professor_wizards = [
    {'name':'덤블도어', 'age':116},
    {'name':'맥고나걸', 'age':85},
    {'name':'스네이프', 'age':60},
]

# 마법사 이름을 받으면 list에서 찾아서 age 리턴
def get_age(name, wizards):
    for wizard in wizards:
        if wizard['name'] == name:
            return wizard['age']
    return ('교수님이 아닙니다')

print(get_age('덤블도어', professor_wizards))
print(get_age('맥고나걸', professor_wizards))
print(get_age('해리', professor_wizards))

