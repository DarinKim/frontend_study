# python Requests 라이브러리 사용 & 파이썬 기초 문법 연습
# 서울시 OpenAPI 사용 & List/Dictionary/함수/if/for 연습

# requests 라이브러리 설치 필요
import requests

# requests를 사용해 요청(Request) 하기
response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

# 응답(response) 데이터만 json을 쉽게 접근할 수 있게 만들어 city_air에 담고
city_air = response_data.json()
# 값을 출력
print(city_air['RealtimeCityAir']['row'][0]['NO2'])

# 모든 구의 PM10 값 출력
gu_infos = city_air['RealtimeCityAir']['row']
for gu_info in gu_infos:
    print(gu_info['MSRSTE_NM'], gu_info['PM10'])

print('=========')
# PM10 값이 20미만인 구만 찍자
gu_infos = city_air['RealtimeCityAir']['row']
for gu_info in gu_infos:
    if gu_info['PM10'] < 30:
        print(gu_info['MSRSTE_NM'], gu_info['PM10'])
