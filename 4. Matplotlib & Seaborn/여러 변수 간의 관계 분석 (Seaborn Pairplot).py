# 문제 2: 여러 변수 간의 관계 분석 (Seaborn Pairplot)
# 💡 학생들의 키, 몸무게, 시험 점수 간의 관계를 한눈에 볼 수 있도록 시각화하세요.

# ✅ 추가 요구사항
# sns.pairplot()을 사용하여 여러 컬럼 간의 관계를 분석
# 산점도와 히스토그램을 동시에 확인할 수 있도록 시각화
# hue="성별"을 추가하여 성별(남/여) 차이를 비교
# 📌 데이터 제공:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# 폰트 설정 (나눔고딕 사용)
mpl.rc('font', family='NanumGothic')

data = {
    "키(cm)": [160, 165, 170, 175, 180, 155, 167, 172, 178, 182],
    "몸무게(kg)": [55, 60, 65, 70, 75, 50, 62, 68, 73, 78],
    "시험 점수": [80, 85, 90, 95, 70, 75, 88, 92, 85, 89],
    "성별": ["남", "남", "남", "남", "남", "여", "여", "여", "여", "여"]
}

df = pd.DataFrame(data)

sns.pairplot(df, kind="scatter", diag_kind="kde")
plt.show()

# plt.figure(figsize=(8,6))
# sns.scatterplot(x=df["키(cm)"], y=df["몸무게(kg)"], hue=df["시험 점수"], palette="coolwarm", s=100)
# plt.xlabel("키 (cm)")
# plt.ylabel("몸무게 (kg)")
# plt.title("키와 몸무게 관계 (시험 점수에 따른 색상)")
# plt.show()