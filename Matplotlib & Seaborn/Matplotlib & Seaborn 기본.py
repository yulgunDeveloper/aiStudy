# import matplotlib.pyplot as plt

# # 데이터 생성
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 50]

# # 그래프 그리기
# plt.plot(x, y, marker='o', linestyle='-', color='b', label="선 그래프")
# plt.xlabel("X축")
# plt.ylabel("Y축")
# plt.title("Matplotlib 선 그래프 예제")
# plt.legend()
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt

# # 샘플 데이터 생성
# tips = sns.load_dataset("tips")  # Seaborn 제공 샘플 데이터

# # 산점도 그래프 그리기
# sns.scatterplot(x="total_bill", y="tip", data=tips)

# plt.title("Seaborn 산점도 예제")
# plt.show()


# 문제 1: 선 그래프(Line Plot) 그리기
# 다음 데이터를 이용하여 "연도별 매출 변화"를 나타내는 선 그래프를 그려보세요.
# X축: 연도 (2018년 ~ 2023년)
# Y축: 매출 (단위: 억 원)

# import matplotlib.pyplot as plt
# import matplotlib as mpl

# # 폰트 설정 (나눔고딕 사용)
# mpl.rc('font', family='NanumGothic')

# years = [2018, 2019, 2020, 2021, 2022, 2023]
# sales = [50, 65, 70, 90, 85, 120]

# plt.plot(years, sales, marker='o', linestyle='-', color='g', label="선 그래프")
# plt.xlabel("연도 (2018년 ~ 2023년)")
# plt.ylabel("매출 (단위: 억 원)")
# plt.title("연도별 매출 변화")
# plt.legend()
# plt.show()


# 문제 2: 막대 그래프(Bar Chart) 그리기
# 다음 데이터를 이용하여 "부서별 평균 급여"를 나타내는 막대 그래프를 그려보세요.
# X축: 부서
# Y축: 평균 급여 (단위: 만 원)

departments = ["영업", "개발", "디자인", "인사", "마케팅"]
salaries = [350, 500, 400, 320, 450]

# 🔹 추가 요구사항
# 막대 색상을 하늘색(skyblue)으로 설정하세요.
# 그래프 제목과 X, Y 축 라벨을 추가하세요.
# X축 글자가 겹치지 않도록 회전(rotation)하세요.

# import matplotlib.pyplot as plt
# import matplotlib as mpl

# # 폰트 설정 (나눔고딕 사용)
# mpl.rc('font', family='NanumGothic')

# plt.figure(figsize=(8, 5)) 
# plt.bar(departments, salaries, color='skyblue')
# plt.title("부서별 평균 급여")
# plt.xlabel("부서")
# plt.ylabel("평균 급여 (단위: 만 원)")
# plt.xticks(rotation=30)
# plt.show()

# 문제 3: 산점도 (Scatter Plot) 그리기
# 다음 데이터를 이용하여 "공부 시간과 시험 점수 관계"를 나타내는 산점도를 그려보세요.
# X축: 공부 시간 (시간)
# Y축: 시험 점수

study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [45, 50, 55, 65, 70, 72, 80, 85, 90, 95]

# 🔹 추가 요구사항
# 점 색상을 빨간색(red)으로 설정하세요.
# 점 크기는 100으로 설정하세요. (s=100)
# 그래프 제목과 X, Y 축 라벨을 추가하세요.


# import matplotlib.pyplot as plt
# import matplotlib as mpl

# 폰트 설정 (나눔고딕 사용)
# mpl.rc('font', family='NanumGothic')

# plt.scatter(study_hours, exam_scores, color="red", s=100)
# plt.xlabel("공부 시간 (시간)")
# plt.ylabel("시험 점수")
# plt.title("공부 시간과 시험 점수 관계")
# plt.show()

# import seaborn as sns
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl

# # 폰트 설정 (나눔고딕 사용)
# mpl.rc('font', family='NanumGothic')

# # 예제 데이터
# data = {
#     "키(cm)": [150, 160, 165, 170, 175],
#     "몸무게(kg)": [50, 55, 60, 70, 75],
#     "시험 점수": [70, 80, 85, 90, 95]
# }

# df = pd.DataFrame(data)

# # 상관계수 히트맵(1에 가까울수록 → 두 변수는 강한 양의 상관관계, 0에 가까울수록 → 두 변수는 거의 관련 없음, -1에 가까울수록 → 두 변수는 강한 음의 상관관계)
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Feature Correlation Heatmap")
# plt.show()

# import seaborn as sns
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl

# # 폰트 설정 (나눔고딕 사용)
# mpl.rc('font', family='NanumGothic')

# # 예제 데이터
# data = {
#     "키(cm)": [150, 160, 165, 170, 175],
#     "몸무게(kg)": [50, 55, 60, 70, 75],
#     "시험 점수": [70, 80, 85, 90, 95]
# }

# df = pd.DataFrame(data)

# # KDE 플롯
# plt.figure(figsize=(8, 6))
# sns.kdeplot(df["키(cm)"], label="키(cm)", fill=True)
# sns.kdeplot(df["몸무게(kg)"], label="몸무게(kg)", fill=True)
# sns.kdeplot(df["시험 점수"], label="시험 점수", fill=True)

# plt.xlabel("값")
# plt.ylabel("밀도")
# plt.title("KDE Plot of Features")
# plt.legend()
# plt.show()


# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib as mpl

# # 폰트 설정 (나눔고딕 사용)
# mpl.rc('font', family='NanumGothic')

# # 예제 데이터
# data = {
#     "시험 점수": [70, 80, 85, 90, 95, 78, 88, 92, 76, 84, 79, 81, 87, 93, 89]
# }

# df = pd.DataFrame(data)

# # KDE 플롯 (시험 점수)
# plt.figure(figsize=(8, 6))
# sns.kdeplot(df["시험 점수"], fill=True, color="blue", linewidth=2)

# plt.xlabel("시험 점수")
# plt.ylabel("밀도")
# plt.title("시험 점수 분포 KDE Plot")
# plt.grid(True)  # 격자 추가
# plt.show()
