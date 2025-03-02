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

# user_list = []

# class User:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#         user_list.append({"name": name, "age": age, "email": email})  # 딕셔너리 저장


#     @staticmethod
#     def search():
#         검색할_이름 = input("검색할 회원 이름을 입력하세요: ")
#         for user in user_list:
#             if user["name"] == 검색할_이름:  # 리스트에서 해당 이름 찾기
#                 print(f"이름: {user['name']}, 나이: {user['age']}, 이메일: {user['email']}")
#                 return  # 찾았으면 함수 종료
#         print("회원 정보를 찾을 수 없습니다.")  # 리스트에 없을 경우


# user1 = User("Alice", 25, "alice@example.com")
# user2 = User("Bob", 30, "bob@example.com")
# user3 = User("Charlie", 22, "charlie@example.com")

# User.search()


# 문제 2: 도서 관리 시스템 (딕셔너리 활용)
# 요구사항:
# 도서관에서 책을 관리하는 프로그램을 작성하시오.
# 책 데이터는 책 제목(title)을 키(key)로, 저자(author)와 출판연도(year)를 값(value)으로 가지는 딕셔너리에 저장하시오.
# 사용자가 책 제목을 입력하면 해당 책의 정보를 출력하도록 하시오.

# 사용자 입력
# 검색할_책 = input("검색할 책 제목을 입력하세요: ") 

도서목록 = {}
class BookManagement:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        도서목록[title] = {"author": author, "year": year}  # 딕셔너리 추가

    @staticmethod
    def search():
        검색할_책 = input("검색할 책 제목을 입력하세요: ")

        for title in 도서목록:
            if 검색할_책 == title:
                print("책 제목:", 검색할_책)
                print("저자:", 도서목록[검색할_책]["author"])
                print("출판연도:", 도서목록[검색할_책]["year"])
            else:
                print("책을 찾을 수 없습니다.")

    @staticmethod
    def add_book(title, author, year):
        if title in 도서목록:
            print(f"'{title}' 책이 이미 존재합니다.")
        else:
            도서목록[title] = {"author": author, "year": year}
            print(f"'{title}' 책이 추가되었습니다.")
    
    @staticmethod   
    def del_book(title):
        if title in 도서목록:
            del 도서목록[title]
            print(f"'{title}' 책이 삭제되었습니다.")
        else:
            print("삭제할 책이 없습니다.")  # 책이 없을 때 메시지 추가


book1 = BookManagement("Python Basics", "John Doe", 2020)
book2 = BookManagement("Machine Learning", "Jane Smithe", 2019)

# BookManagement.search()
