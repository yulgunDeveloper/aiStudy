# 문제 2: 손글씨 숫자 예측
# 손글씨 숫자 데이터셋(MNIST)을 사용하여, 주어진 숫자 이미지에서 숫자를 예측하세요.

# 주어진 데이터셋:
# MNIST는 28x28 크기의 손글씨 숫자 이미지로 이루어진 데이터셋입니다.
# 각 이미지는 0부터 9까지의 숫자 중 하나에 해당합니다.
# 과제:
# 1. MNIST 데이터셋을 로드하세요.
# 2. 훈련 데이터와 테스트 데이터를 나누고, 이미지 데이터를 1차원 배열로 변환하세요.
# 3. 로지스틱 회귀(Logistic Regression) 모델을 사용하여 훈련시키세요.
# 4. 테스트 데이터셋을 사용하여 모델을 평가하고, 예측 결과를 출력하세요.
# 5. 예측된 숫자와 실제 숫자를 비교하여 정확도를 확인하세요.

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 데이터셋 정보 확인
# print(f"훈련 데이터 개수: {x_train.shape[0]}")
# print(f"테스트 데이터 개수: {x_test.shape[0]}")

# 이미지의 크기 확인
# print(f"각 이미지는 {x_train.shape[1]}x{x_train.shape[2]} 크기입니다.")

# 이미지 데이터를 1차원 배열로 변환 (28x28 이미지를 784 크기의 벡터로 변환)
x_train_flat = x_train.reshape(x_train.shape[0], -1)  # (60000, 28, 28) -> (60000, 784)
x_test_flat = x_test.reshape(x_test.shape[0], -1)  # (10000, 28, 28) -> (10000, 784)

# 데이터 스케일링 (StandardScaler로 데이터 정규화)
scaler = StandardScaler()
x_train_scaled  = scaler.fit_transform(x_train_flat)
x_test_scaled = scaler.transform(x_test_flat)

# 로지스틱 회귀 모델 생성 및 훈련
model = LogisticRegression(max_iter=100, solver='lbfgs', multi_class='auto', random_state=42)
model.fit(x_train_scaled, y_train)

# 테스트 데이터셋을 사용하여 모델을 평가하고, 예측 결과를 출력
y_pred = model.predict(x_test_scaled)
# print(y_result)

# 예측된 숫자와 실제 숫자를 비교하여 정확도를 확인
accuracy = accuracy_score(y_test, y_pred)
print(f"예측 정확도: {accuracy * 100:.2f}%")