# 📌 문제 1: 고객 데이터 클러스터링 (K-Means 활용)
# 한 회사가 고객 데이터를 수집했어.
# 하지만 고객을 어떤 기준으로 분류해야 할지 모르기 때문에 비지도학습을 사용하여 고객을 군집화하려고 해.
# ✅ 데이터셋 정보 (예제)
# 고객 ID	나이	연간 소득(만원)	지출 점수 (1~100)
# 1	25	3000	80
# 2	35	5000	20
# 3	40	7000	50
# ...	...	...	...
# 💡 문제:
# 1. K-Means를 사용하여 고객을 3개의 그룹으로 군집화하세요.
# 2. 군집화 결과를 시각화하여 각 그룹이 어떻게 나뉘는지 확인하세요.
# 3. 각 군집의 특징을 분석하고, 어떤 그룹이 어떤 고객을 포함하는지 해석해 보세요.

# import pandas as pd

# # 고객 데이터 생성
# customer_data = {
#     "CustomerID": range(1, 21),
#     "Age": [25, 35, 40, 22, 50, 30, 28, 45, 33, 38,
#             27, 48, 29, 52, 42, 31, 26, 47, 37, 34],
#     "AnnualIncome": [3000, 5000, 7000, 2500, 10000, 5500, 4200, 8200, 4900, 6200,
#                      3900, 9100, 4100, 10200, 7300, 4600, 3400, 8700, 5900, 5300],
#     "SpendingScore": [80, 20, 50, 90, 30, 60, 75, 40, 55, 45,
#                       85, 35, 78, 25, 48, 72, 88, 38, 58, 63]
# }

# # 데이터프레임 생성
# df = pd.DataFrame(customer_data)

# # CSV 파일 저장
# file_path = "C:/Users/권유림/Desktop/aiStudy/customer_data.csv"
# df.to_csv(file_path, index=False)

# # 파일 경로 반환
# file_path

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. 데이터 로드
customer_data = pd.read_csv("C:/Users/권유림/Desktop/aiStudy/customer_data.csv")

# 2. 필요한 특성 선택 (예: 연령, 연 소득, 총 구매 금액)
X = customer_data[['Age', 'AnnualIncome', 'SpendingScore']]

# 3. K-Means 모델 적용
kmeans = KMeans(n_clusters=3, random_state=42)  # 3개의 그룹으로 클러스터링
customer_data['Cluster'] = kmeans.fit_predict(X)

# 4. 클러스터 시각화 (연소득 vs 총 구매 금액)
plt.scatter(customer_data['AnnualIncome'], customer_data['SpendingScore'], c=customer_data['Cluster'], cmap='viridis')
plt.xlabel("Annual Income")
plt.ylabel("SpendingScore")
plt.title("Customer Segmentation using K-Means")
plt.show()

