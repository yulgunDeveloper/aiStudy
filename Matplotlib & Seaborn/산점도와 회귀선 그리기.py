# 문제 1: 산점도와 회귀선 그리기 (Seaborn)
# 💡 어떤 제품의 광고비와 매출 간의 관계를 분석하는 산점도를 그리세요.

# ✅ 추가 요구사항
# sns.scatterplot()을 사용하여 광고비와 매출 간의 관계를 시각화
# sns.regplot()을 사용하여 회귀선(추세선)을 추가
# 광고비가 많을수록 매출이 증가하는지 확인하세요.
# 📌 데이터 제공:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "광고비(만원)": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    "매출(만원)": [100, 120, 150, 180, 210, 250, 270, 300, 320, 350]
}

df = pd.DataFrame(data)
# plt.scatter(df["광고비(만원)"], df["매출(만원)"])
sns.scatterplot(x=df["광고비(만원)"], y=df["매출(만원)"], color="blue", s=100)

# 회귀선 추가
sns.regplot(x=df["광고비(만원)"], y=df["매출(만원)"], scatter=False, color="red")

plt.xlabel("광고비 (만원)")
plt.ylabel("매출 (만원)")
plt.title("광고비와 매출의 관계")
plt.show()