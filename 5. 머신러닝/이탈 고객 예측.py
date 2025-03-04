# 문제 3: 이탈 고객 예측
# 주어진 고객 데이터에서 고객이 이탈할지 여부를 예측하는 모델을 만드세요.

# 주어진 데이터셋:
# 각 고객에 대한 정보를 기반으로 이탈 여부를 예측하는 문제입니다.
# 데이터에는 고객 나이, 성별, 서비스 사용 기간, 월 요금 등의 정보가 포함되어 있습니다.
# 과제:
# 1. 고객 데이터셋을 로드하고, 결측치가 있는지 확인하세요.
# 2. 결측치를 적절히 처리하고, 데이터를 훈련과 테스트로 나누세요.
# 3. 정규화
# 4. 로지스틱 회귀 모델을 사용하여 훈련시키세요.
# 5. 테스트 데이터셋에 대해 고객이 이탈할지 여부를 예측하세요.
# 6. 예측된 결과와 실제 이탈 여부를 비교하여 정확도를 평가하세요.

# import pandas as pd

# # 데이터 생성
# data = {
#     "고객 ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "나이": [25, 40, 35, 50, 29, 60, 42, 36, 31, 55],
#     "성별": ["남성", "여성", "남성", "여성", "남성", "여성", "남성", "여성", "남성", "여성"],
#     "서비스 사용 기간 (개월)": [12, 24, 6, 36, 18, 48, 2, 12, 8, 24],
#     "월 요금": [70.5, 85.3, 60.0, 100.0, 75.5, 120.0, 65.0, 80.0, 68.0, 95.0],
#     "이탈 여부": [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
# }

# # DataFrame으로 변환
# df = pd.DataFrame(data)

# # CSV로 저장
# df.to_csv('customer_churn_data.csv', index=False, encoding='utf-8')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score

# 1. 데이터셋 로드
data_set = pd.read_csv("C:/Users/권유림/Desktop/aiStudy/customer_churn_data.csv")
print("결측치 개수:", data_set.isnull().sum()) #결측치 확인

# 2. 결측치를 적절히 처리하고, 데이터를 훈련과 테스트로 나누세요.
# 결측치 처리는 보통 평균값, 제거 등으로 한다.
# # 평균값 처리
# mean_age = data_set["나이"].mean()  # '나이' 컬럼의 평균값 계산
# data_set["나이"].fillna(mean_age, inplace=True)  # NaN 값을 평균값으로 대체

# #제거
# data_set = data_set.dropna()

# 성별 컬럼을 0과 1로 변환 (남성은 0, 여성은 1)
label_encoder = LabelEncoder()
data_set["성별"] = label_encoder.fit_transform(data_set["성별"])

# 특성과 타겟 분리
X = data_set.drop(columns=['이탈 여부'])
y = data_set['이탈 여부']

# 훈련 데이터와 테스트 데이터로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# 3. 정규화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. 로지스틱 회귀 모델을 사용하여 훈련시키세요.
model = LogisticRegression(max_iter=100, solver='lbfgs', random_state=42)
model.fit(X_train_scaled, y_train)

# 5. 테스트 데이터셋에 대해 고객이 이탈할지 여부를 예측하세요.
y_pred = model.predict(X_test_scaled)

# # 6. 예측된 결과와 실제 이탈 여부를 비교하여 정확도를 평가하세요.
# accuracy = accuracy_score(y_test, y_pred)
# print(f"예측 결과 정확도: {accuracy * 100:.2f}%")

# Recall을 사용하여 평가
recall = recall_score(y_test, y_pred)
print(f"이탈 여부 Recall: {recall * 100:.2f}%")