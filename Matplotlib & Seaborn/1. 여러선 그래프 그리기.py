#  문제 1: 여러 개의 선 그래프 그리기 (Matplotlib)
# 💡 두 개의 제품(Product A, Product B)의 연도별 매출 변화를 한 그래프에 표시하세요.
# ✅ 추가 요구사항:
# 두 선의 색상을 다르게 설정하세요.
# 선마다 라벨을 추가하고, 범례(legend)를 표시하세요.
# 점(marker)을 추가하여 데이터 지점을 강조하세요.
# years = [2018, 2019, 2020, 2021, 2022, 2023]
# sales_A = [50, 65, 70, 90, 85, 120]
# sales_B = [40, 55, 60, 80, 75, 110]

# import matplotlib.pyplot as plt

# years = [2018, 2019, 2020, 2021, 2022, 2023]
# sales_A = [50, 65, 70, 90, 85, 120]
# sales_B = [40, 55, 60, 80, 75, 110]

# plt.plot(years, sales_A, linestyle='-', marker='o', color='b', label="Product A")  # 파란색
# plt.plot(years, sales_B, linestyle='-', marker='s', color='r', label="Product B")  # 빨간색 (네모 모양 마커)

# plt.xlabel("연도")
# plt.ylabel("매출 (억 원)")
# plt.title("연도별 매출 변화")
# plt.legend()  # 범례 추가
# plt.grid(True)  # 격자 추가하면 가독성이 좋아짐

# plt.show()

# 📌 문제 2: 가로 막대 그래프 그리기 (Matplotlib)
# 💡 각 나라별 평균 기대 수명을 나타내는 가로 막대 그래프를 그리세요.
# ✅ 추가 요구사항:
# 막대 색상을 ‘lightcoral’로 설정하세요.
# X축(나라) 레이블을 45도 회전하세요.
# X축 레이블을 "평균 기대 수명(년)"으로 설정하세요.
# countries = ["한국", "미국", "일본", "독일", "프랑스"]
# life_expectancy = [83, 78, 85, 81, 82]


# import matplotlib.pyplot as plt
# import matplotlib as mpl

# # 폰트 설정 (나눔고딕 사용)
# mpl.rc('font', family='NanumGothic')


# plt.barh(countries, life_expectancy, color='lightcoral')
# plt.xlabel("평균 기대 수명 (년)")
# plt.ylabel("나라")
# plt.xticks(rotation=45)  

# # 그래프 제목 추가
# plt.title("각 나라별 평균 기대 수명")

# plt.show()


# 📌 문제 3: 다중 히스토그램 그리기 (Seaborn)
# 💡 두 반(1반, 2반)의 시험 점수 분포를 비교하는 히스토그램을 그리세요.
# ✅ 추가 요구사항:
# alpha=0.5를 사용하여 두 그래프가 겹칠 때 투명도를 조절하세요.
# 각 반의 색상을 다르게 설정하세요.
# bins 개수를 8개로 설정하세요.

class1_scores = [70, 75, 80, 85, 90, 95, 78, 88, 92, 76]
class2_scores = [65, 72, 78, 82, 85, 89, 91, 74, 79, 84]

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# 폰트 설정 (나눔고딕 사용)
mpl.rc('font', family='NanumGothic')

# 히스토그램 그리기
sns.histplot(class1_scores, bins=8, color="blue", alpha=0.5, label="1반")
sns.histplot(class2_scores, bins=8, color="red", alpha=0.5, label="2반")

# 제목 & 라벨 추가
plt.title("1반 vs 2반 시험 점수 분포")
plt.xlabel("시험 점수")
plt.ylabel("학생 수")

# 범례 추가
plt.legend()

# 그래프 출력
plt.show()