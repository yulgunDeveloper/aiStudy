# 1. 1부터 10까지의 숫자 중 짝수만 담은 리스트를 리스트 컴프리헨션을 사용해 만들어보세요.
list = [n for n in range(2, 11, 2)]
print(list)

# 2. "hello" 문자열의 각 문자를 대문자로 변환한 리스트를 리스트 컴프리헨션을 사용해 만들어보세요.
st = "hello"
st = [char.upper() for char in st]
print(st)

# 3. 1부터 10까지의 제곱값을 리스트로 만들어보세요.
one_to_ten_squared = [n ** 2 for n in range(1, 11)]
print(one_to_ten_squared)

# 4. 1부터 20까지의 숫자 중 3의 배수만 담은 리스트를 만들어보세요.
number = [n for n in range(3, 21, 3)]
print(number)

# 5. 주어진 리스트의 요소 중 길이가 3 이상인 문자열만 필터링하여 새 리스트를 만들어보세요.
words = ["a", "the", "apple", "is", "cat", "hi"]

new_list = [word for word in words if len(word) >= 3]
print(new_list)

# 6. 두 개의 리스트를 사용하여 모든 조합의 (x, y) 쌍을 담은 리스트를 만들어보세요.
list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']

new_list = [(x, y) for x in list1 for y in list2]
print(new_list)

# 7. 딕셔너리에서 값이 80 이상인 키만 리스트로 추출하세요.
scores = {'A': 85, 'B': 60, 'C': 90, 'D': 70, 'E': 95}

key_list = [key for key in scores if scores[key] >= 80]
print(key_list)