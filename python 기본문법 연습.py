# 1. 삼성전자라는 변수로 50,000원을 바인딩해보세요.
# 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
평가금액 = 삼성전자 * 10
print(평가금액)

# 2. 다음 표는 삼성전자의 일부 투자정보입니다. 
# 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
# 시가총액	298조
# 현재가	50,000원
# PER	15.79
# 변수 속성의 구체적인 값에 대한 이름, 자료형, 자료값을 할당하는 각각의 과정을 '바인딩'이라고 한다.
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 3. 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.

# >> s = "hello"
# >> t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# 실행 예: hello! python
s = "hello"
t = "python"
print(s + "! " + t)
print(s + "!", t)
# python은 print 안에 ,를 쓰면 띄어쓰기가 된다

# 4. letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0], letters[2])

# 5. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# 실행 예: 2210
license_plate = "24가 2210"
print(license_plate[-4:])

# 6. 아래의 문자열에서 '홀' 만 출력하세요
# 실행 예: 홀홀홀
string = "홀짝홀짝홀짝"
print(string[::2])
# 슬라이싱할 때 `시작인덱스:끝인덱스:오프셋`을 지정할 수 있습니다.

# 7. 문자열을 거꾸로 뒤집어 출력하세요.
# 실행 예: NOHTYP
string = "PYTHON"
print(string[::-1])

# 8. 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 9. 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number1 = phone_number.replace("-", "")
print(phone_number1)

# 10. url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# 실행 예: kr
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[1])
# print(url_split[-1])

# 11. 아래 코드의 실행 결과를 예상해보세요.
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)
# 문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.
# TypeError: 'str' object does not support item assignment

# 12. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
# 실행 예: Abcdfe2A354A32A
string_replace_A = string.replace('a', 'A')
print(string_replace_A)

# 13. 아래 코드의 실행 결과를 예상해보세요.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
# `abcd`가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다.

# 14. 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
t1 = 'python'
t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예: python java python java python java python java
end = t1 + " " + t2 + " "
print(end * 4)

# 15. 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 16. 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(',','')
타입변환 = int(컴마제거)
print(타입변환)
print(타입변환, type(타입변환))

# 17. 다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 18. 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
data = data.strip()
print(data)

# 19. 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# 20. 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
str = "hello"
str = str.capitalize()
print(str)

# 21. 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
tf = file_name.endswith(('xlsx', 'xls'))
print(tf)

# 22. 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
tf = file_name.startswith('2020')
print(tf)

# 23. 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
a_split = a.split()
a_split_1 = a.split(" ")
print(a_split)
print(a_split_1)

# 24. 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
ticker_split = ticker.split('_')
print(ticker_split)

# 25. movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
movie_rank.append("배트맨")
print(movie_rank)

# 26. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 27. movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
del movie_rank[3]
print(movie_rank)

# 28. movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 29. lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 30. 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
print("min: %d" % (min(nums)))
print(f"max: {max(nums)}")
# print("min: ", min(nums))

# 31. 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 32. 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 33. 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
averange = sum(nums) / len(cook)
print(averange)

# 34. price 변수에는 날짜와 종가 정보가 저장돼 있다. 
# 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 35. 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 36. 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 37. 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
# nums.reverse()
print(nums[::-1])

# 38. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시: 삼성전자 Naver
print(interest[0], interest[2])

# 39. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시: 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print(" ".join(interest)) # 어렵다...**

# 40. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# 출력 예시: 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print("/".join(interest))

print("\n".join(interest))

# 41. 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
interest = string.split('/')
print(interest)

# 42. 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
# data2 = sorted(data)
print(data)
# print(data2)

# 43. my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()

# 44. 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 
# 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)

# 45. 숫자 1 이 저장된 튜플을 생성하라.
tup = (1, )
print(type(tup))
# 리스트는 내용을 바꿀 수 있고 튜플은 내용 변경 불가
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작합니다.

# 46. 다음 튜플을 리스트로 리스트를 튜플로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
data = tuple(interest)

data = tuple(range(2, 100, 2)) #range 함수 2 부터 100까지 2씩 커지기
print( data )

# 47. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, 
# start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

# 예시)
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a 0
# >> b 1
# >> c [2, 3, 4, 5]

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b = scores
print(valid_score)

# 48. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때,
#  start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,b, *valid_score = scores
print(valid_score)

# 49.다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
# 이름	희망 가격
# 메로나	1000
# 폴라포	1200
# 빵빠레	1800
icecream = {"메로나" : 1000, "폴라포": 1200, "빵빠레" : 1800}

# 49번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
# 이름	희망 가격
# 죠스바	1200
# 월드콘	1500
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500

# 50. 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격:", ice["메로나"])

# 51. 다음 딕셔너리에서 메로나를 삭제하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

del ice["메로나"]

# 52. 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라.
# 딕셔너리의 이름은 inventory로 한다.
# 이름	가격	재고
# 메로나	300	20
# 비비빅	400	3
# 죠스바	250	100

inventory = {'메로나' : [300, 20],'비비빅' : [400, 3], '죠스바': [250, 100]}

print(inventory["메로나"][0], "원")

inventory["월드콘"] = [500, 7]
print(inventory)

# 53. 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

ice = list(icecream.keys())
print(ice)

ice = list(icecream.values())
print(ice)

# 54.icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라. --어렵다**
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}


print(sum(icecream.values()))


# 55. 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 56. 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
# -- 어렵다**
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
# 실행 예시: print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}
result = dict(zip(keys, vals))
print(result)

# 57. date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
# 실행 예시:
# >> print(close_table) {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}
close_table = dict(zip(date, close_price))
print(close_table)


#  즉, 튜플이나 리스트는 그 자체로 zip을 통해 dict로 만들 수 있다.


# 58. 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# >> 숫자를 입력하세요: 30  40

# a = input(">> 숫자를 입력하세요:")
# print(int(a) + 10)

# 59. 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# >> 30 짝수

# user = input(">> ")
# if int(user) % 2 == 0:
#        print("짝수")
# else:
#        print("홀수")

# 60. 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라.
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# user = input(">> 입력값: ")
# if int(user) + 20 > 255:
#        print(255)
# else:
#        print(int(user) + 20)

# 61. 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다. 
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.

# user = input("입력값: ")
# result = int(user) - 20

# if result < 0:
#     print(0)
# elif result > 255:
#     print(255)
# else:
#     print(result)

# 62. 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# >> 현재시간:02:00
# 정각 입니다.

# user = input("현재시간:")
# back = user.split(":")
# if back[1] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

# split 말고 다음과 같이 사용할 수도 있다.
# user[-2:] == "00"

# 63. 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = ["사과", "포도", "홍시"]
# >> 좋아하는 과일은? 사과
# 정답입니다.

# user = input("좋아하는 과일은? ")

# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 64. 아래와 같이 fruit 딕셔너리가 정의되어 있다. 
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 제가좋아하는계절은: 봄
# 정답입니다.

# user = input("제가좋아하는계절은: ")
# if user in fruit.keys():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 65. 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# user = input("")
# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())

# 66. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E

# score = input("score: ")
# if 81 <= int(score) <= 100:
#     print("grade is A")
# elif 61 <= int(score) <= 80:
#     print("grade is B")
# elif 41 <= int(score) <= 60:
#     print("grade is C")
# elif 21 <= int(score) <= 40:
#     print("grade is D")
# else:
#     print("grade is E")

# 67. 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 
# 각 통화별 환율은 다음과 같다. 
# 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171

# -- 어렵다**
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}

# user = input("입력: ")
# rate, currency = user.split(" ")
# print(환율[currency] * float(rate), "원")


# 68. 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20

# num1 = input("input number1: ")
# num2 = input("input number2: ")
# num3 = input("input number3: ")
# m_list = [int(num1), int(num2), int(num3)]
# print(max(m_list))

# 69. 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음

# call = {"011": "SKT", "016": "KT", "019": "LGU", "010": "알수없음"}
# user_num = input("휴대전화 번호 입력: ")
# where = user_num.split("-")
# 통신사 = call[where[0]]
# print(f"당신은 {통신사} 사용자입니다.")

# 70. 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5 
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다. 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.

# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.

# user_num = input("주민등록번호:")
# user_num = user_num.replace("-", "")
# mul = (2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5)
# n = 0
# sum = 0
# for i in mul:
#        sum += int(user_num[n]) * i
#        n = n + 1
# result = 11 - sum % 11
# if int(user_num[-1:]) == result:
#        print("유효한 주민등록번호입니다.")
# else:
#        print("유효하지 않은 주민등록번호입니다.")

# 131부터 시작
