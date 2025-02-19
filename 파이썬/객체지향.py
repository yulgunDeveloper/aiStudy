# 학생(Student) 클래스를 설계하고, 객체를 생성해보세요.
# 속성(Attributes): 이름(name), 나이(age), 성적(grades) (리스트 형태)
# 메서드(Methods): 성적 추가(add_grade), 평균 성적 계산(calculate_average)

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        result = 0
        for num in self.grades:
            result += num
        result /= len(self.grades)
        return print(f"{self.name}의 평균 성적:", result)
    
student = Student("Lee", 20)
student.add_grade(90)
student.add_grade(85)
student.add_grade(95)
student.calculate_average()