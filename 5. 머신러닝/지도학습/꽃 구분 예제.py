import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1️⃣ 붓꽃 데이터셋 불러오기
iris = datasets.load_iris()
X = iris.data  # 꽃의 특징 (꽃잎 길이, 너비 등)
y = iris.target  # 꽃의 품종 (0: Setosa, 1: Versicolor, 2: Virginica)

# 2️⃣ 데이터 분할 (훈련 80%, 테스트 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3️⃣ 데이터 정규화 (스케일링)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4️⃣ K-최근접 이웃(KNN) 분류기 모델 생성
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)  # 모델 학습

# 5️⃣ 예측 및 평가
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"모델 정확도: {accuracy * 100:.2f}%")

# 6️⃣ 새로운 꽃 데이터 예측
new_flower = np.array([[5.0, 3.2, 1.2, 0.2]])  # 새로운 꽃의 특성
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)

print("새로운 꽃의 예측된 품종:", iris.target_names[prediction[0]])
