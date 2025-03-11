# 📌 문제 2: 차원 축소 (PCA 활용)
# 고차원 데이터셋을 다루다 보면 데이터 차원이 너무 커서 분석이 어려운 경우가 있어.
# 이럴 때 PCA (Principal Component Analysis)를 사용하여 데이터를 저차원으로 축소할 수 있어.
# ✅ 데이터셋 정보 (예제)
# X(10차원) 데이터가 주어져 있음
# 각 열은 서로 다른 특성을 나타냄
# 💡 문제:
# 1. 주어진 X(10차원) 데이터를 PCA를 사용하여 2차원으로 축소하세요.
# 2. 차원 축소된 데이터를 시각화하고, 원본 데이터와 비교하여 설명하세요.
# 3. 축소된 2차원 데이터에서 중요한 특징을 발견할 수 있는지 분석하세요.

# import pandas as pd
# import numpy as np

# # 랜덤 데이터 생성 (100개의 샘플, 10개의 특성)
# np.random.seed(42)
# data = np.random.rand(100, 10)  # 0~1 사이의 랜덤 값 생성

# # 컬럼 이름 생성 (Feature_1, Feature_2, ..., Feature_10)
# columns = [f'Feature_{i+1}' for i in range(10)]

# # 데이터프레임 생성
# df = pd.DataFrame(data, columns=columns)

# # CSV 파일로 저장
# df.to_csv("pca_sample_data.csv", index=False)

# print("pca_sample_data.csv 파일이 생성되었습니다!")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 📌 1. 데이터 불러오기
df = pd.read_csv("pca_sample_data.csv")

# 📌 2. 데이터 정규화 (PCA는 정규화된 데이터를 사용할 때 성능이 더 좋음)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# 📌 3. PCA 적용 (10차원 -> 2차원 축소)
pca = PCA(n_components=2)  # 2개의 주성분으로 축소
X_pca = pca.fit_transform(scaled_data)

# 📌 4. 축소된 데이터 시각화
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7, edgecolors='k')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - 10D → 2D 데이터 변환 결과")
plt.grid()
plt.show()

# 📌 5. 주성분 분석 결과 출력
explained_variance = pca.explained_variance_ratio_  # 각 주성분이 설명하는 분산 비율
print(f"첫 번째 주성분이 설명하는 분산 비율: {explained_variance[0]:.4f}")
print(f"두 번째 주성분이 설명하는 분산 비율: {explained_variance[1]:.4f}")
print(f"총 설명 가능한 분산 비율: {sum(explained_variance):.4f}")

# 📌 6. PCA 이후 주요 특징 분석
print("\nPCA 주성분 (Feature 중요도)")
print(pd.DataFrame(pca.components_, columns=df.columns, index=["PC1", "PC2"]))
