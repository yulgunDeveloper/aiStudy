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

# 054부터 ㄱㄱ
