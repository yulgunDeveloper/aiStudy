# 문제 1: 회원 정보 관리 (리스트 & 딕셔너리 활용)
# 요구사항:
# 사용자의 정보를 저장하는 프로그램을 작성하시오.
# 각 사용자는 이름(name), 나이(age), 이메일(email) 정보를 가진다.
# 회원 정보는 여러 명을 저장할 수 있어야 하며, 리스트와 딕셔너리를 활용하여 관리해야 한다.
# 사용자의 이름을 입력하면 해당 회원의 정보를 검색하여 출력하시오.

# 예제 데이터 저장
# 회원목록 = [
#     {"name": "Alice", "age": 25, "email": "alice@example.com"},
#     {"name": "Bob", "age": 30, "email": "bob@example.com"},
#     {"name": "Charlie", "age": 22, "email": "charlie@example.com"}
# ]

# 사용자 검색
# 검색할_이름 = input("검색할 회원 이름을 입력하세요: ")  # 예: Alice
# 🔥 심화: 사용자가 새로운 회원을 추가할 수 있도록 기능을 확장해보세요.

user_list = []

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        user_list.append({"name": name, "age": age, "email": email})  # 딕셔너리 저장


    @staticmethod
    def search():
        검색할_이름 = input("검색할 회원 이름을 입력하세요: ")
        for user in user_list:
            if user["name"] == 검색할_이름:  # 리스트에서 해당 이름 찾기
                print(f"이름: {user['name']}, 나이: {user['age']}, 이메일: {user['email']}")
                return  # 찾았으면 함수 종료
        print("회원 정보를 찾을 수 없습니다.")  # 리스트에 없을 경우


user1 = User("Alice", 25, "alice@example.com")
user2 = User("Bob", 30, "bob@example.com")
user3 = User("Charlie", 22, "charlie@example.com")

User.search()


# 문제 2: 도서 관리 시스템 (딕셔너리 활용)