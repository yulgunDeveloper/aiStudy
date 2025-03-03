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

import pandas as pd

test_data = pd.read_csv("C:/Users/권유림/Desktop/aiStudy/5. 머신러닝/Telco Customer Churn/test.csv")
train_data = pd.read_csv("C:/Users/권유림/Desktop/aiStudy/5. 머신러닝/Telco Customer Churn/train.csv")
validation_data = pd.read_csv("C:/Users/권유림/Desktop/aiStudy/5. 머신러닝/Telco Customer Churn/validation.csv")
