# import pandas as pd
# import numpy as np

# # 랜덤 데이터 생성
# np.random.seed(42)
# num_students = 100

# data = {
#     "이름": [f"학생{i+1}" for i in range(num_students)],
#     "키(cm)": np.random.randint(150, 190, num_students),
#     "몸무게(kg)": np.random.randint(45, 90, num_students),
#     "수학 점수": np.random.randint(50, 100, num_students),
#     "영어 점수": np.random.randint(50, 100, num_students),
#     "과학 점수": np.random.randint(50, 100, num_students),
# }

# df = pd.DataFrame(data)

# # CSV 파일 저장
# df.to_csv("sample_students.csv", index=False)

# print("✅ sample_students.csv 파일이 생성되었습니다!")


# 📌 문제 3: 데이터 시각화 (Seaborn & Matplotlib)
# ✅ 문제 3-1: 히스토그램을 사용해 특정 변수의 분포를 확인하세요.
# 🎯 수행 목표:
# 학생들의 수학 점수 분포를 히스토그램으로 나타내세요.
# bins=8로 설정하여 점수 구간을 나누세요.
# Matplotlib 또는 Seaborn을 사용하세요.

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import seaborn as sns

# 폰트 설정 (나눔고딕 사용)
mpl.rc('font', family='NanumGothic')

# df = pd.read_csv('sample_students.csv')
# print(df)

# sns.histplot(df["수학 점수"], bins=8, color="royalblue", kde=True)

# # 그래프 제목 및 축 라벨 추가
# plt.title("학생들의 수학 점수 분포", fontsize=14)
# plt.xlabel("수학 점수", fontsize=12)
# plt.ylabel("학생 수", fontsize=12)
# plt.show()

# ✅ 문제 3-2: 상관계수 히트맵을 사용하여 변수 간 관계를 분석하세요.
# 🎯 수행 목표:
# 학생들의 키, 몸무게, 수학 점수, 영어 점수, 과학 점수 간의 상관관계를 분석하세요.
# sns.heatmap()을 이용하여 히트맵을 그리세요.
# annot=True 옵션을 사용하여 상관계수를 표기하세요.

df = pd.read_csv('sample_students.csv')

df_numeric = df.drop(columns=["이름"])  # "이름" 대신 실제 컬럼명 확인 필요

# 🔹 변수 간 상관계수 계산
correlation_matrix = df_numeric.corr()

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()

