# 기능 요구사항
# 사용자는 두 개의 숫자와 연산자를 입력하면, 프로그램이 계산 결과를 출력해야 한다.
# 지원해야 하는 연산자는 다음과 같다:

# 덧셈 (+)
# 뺄셈 (-)
# 곱셈 (*)
# 나눗셈 (/)
# 나머지 연산 (%)
# 거듭제곱 (**)

class Calculator:
    def __init__(self, a, b, 연산자):
        self.a = a
        self.b = b
        self.연산자 = 연산자

    def plus(self):
        result = self.a + self.b
        return print(result)

    def minus(self):
        result = self.a - self.b
        return print(result)
    
    def multi(self):
        result = self.a * self.b
        return print(result)
    
    def division(self):
        try:
            result = self.a / self.b
            return print(result)
        except:
            return print("숫자는 0으로 나눌 수 없습니다.")
        
    def remainder(self):
        try:
            result = self.a % self.b
            return print(result)
        except:
            return print("숫자는 0으로 나눌 수 없습니다.")
        
    def exponentiation(self):
            result = self.a ** self.b
            return print(result)