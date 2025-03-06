# import pandas as pd
# import numpy as np

# # 랜덤 데이터 생성
# data = {
#     'PassengerId': np.arange(1, 101),
#     'Pclass': np.random.choice([1, 2, 3], 100, p=[0.2, 0.3, 0.5]),  # 객실 등급
#     'Sex': np.random.choice(['male', 'female'], 100, p=[0.6, 0.4]),  # 성별
#     'Age': np.random.randint(1, 80, 100),  # 나이 (1~80세)
#     'SibSp': np.random.randint(0, 5, 100),  # 형제/배우자 수
#     'Parch': np.random.randint(0, 4, 100),  # 부모/자녀 수
#     'Fare': np.round(np.random.uniform(5, 300, 100), 2),  # 티켓 요금 (5~300달러)
#     'Embarked': np.random.choice(['C', 'Q', 'S'], 100, p=[0.2, 0.1, 0.7]),  # 출발지
#     'Survived': np.random.choice([0, 1], 100, p=[0.6, 0.4])  # 생존 여부
# }

# # 데이터프레임 생성
# df = pd.DataFrame(data)

# # CSV 파일 저장
# df.to_csv("titanic_sample_data.csv", index=False)

# 문제 5:주어진 승객 데이터셋을 기반으로 승객이 생존했는지 여부를 예측하는 모델을 만드세요.
# 1. 데이터 로드 및 탐색
# Titanic 데이터셋을 불러오세요.
# 데이터에 결측치가 있는지 확인하세요.
# 필요한 경우 결측치를 처리하세요.
# 2. 특성 선택 및 전처리
# 사용할 특성(Feature)을 선택하세요. (예: Pclass, Sex, Age, SibSp, Parch, Fare 등)
# 성별(Sex)과 같은 범주형 데이터를 숫자로 변환하세요.
# 필요하면 데이터를 정규화하세요.
# 3. 훈련 데이터와 테스트 데이터 분리
# 데이터를 훈련 데이터(Training set)와 테스트 데이터(Test set)로 나누세요.
# 일반적으로 80% 훈련, 20% 테스트로 나눕니다.
# 4. 머신러닝 모델 학습
# LogisticRegression, RandomForestClassifier, 또는 XGBoost 등의 분류 모델을 사용하여 학습하세요.
# GridSearchCV를 활용해 하이퍼파라미터 튜닝을 시도해보세요.
# 5. 모델 평가
# 정확도(Accuracy), 정밀도(Precision), 재현율(Recall), F1-score 등을 사용하여 모델을 평가하세요.
# 혼동 행렬(Confusion Matrix)도 확인하세요.

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from sklearn.metrics import accuracy_score

titanic_sample_data = pd.read_csv("C:/Users/권유림/Desktop/aiStudy/titanic_sample_data.csv", encoding='utf-8')

# 데이터에 결측치가 있는지 확인
print("결측치 개수:", titanic_sample_data.isnull().sum())

# 2. 특성 선택 및 전처리
label_encoders = {}
for col in ['Sex', 'Embarked']:
    le = LabelEncoder()
    titanic_sample_data[col] = le.fit_transform(titanic_sample_data[col])
    label_encoders[col] = le  # 나중에 inverse_transform을 위해 저장

# 정규화
X = titanic_sample_data.drop(columns = "Survived")
y = titanic_sample_data["Survived"]

# 3. 훈련 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. 머신러닝 모델 학습
model = LogisticRegression(max_iter=100, solver='lbfgs', random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

# 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print(f"Optimized Model Accuracy: {accuracy:.2f}%")

