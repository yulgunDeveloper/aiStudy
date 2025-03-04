# import pandas as pd
# import numpy as np

# # 랜덤 시드 설정 (재현 가능성 위해)
# np.random.seed(42)

# # 영화 특성 (예: 장르, 감독, 출연 배우 등)
# genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance']
# directors = ['Steven Spielberg', 'Martin Scorsese', 'Christopher Nolan', 'Quentin Tarantino', 'James Cameron']
# actors = ['Leonardo DiCaprio', 'Brad Pitt', 'Tom Hanks', 'Scarlett Johansson', 'Robert Downey Jr.']

# # 데이터 생성
# data = {
#     '장르': np.random.choice(genres, 50),  # 장르 랜덤 선택
#     '감독': np.random.choice(directors, 50),  # 감독 랜덤 선택
#     '출연 배우': np.random.choice(actors, 50),  # 출연 배우 랜덤 선택
#     '상영 시간': np.random.randint(90, 180, 50),  # 상영 시간 (90~180분)
#     '예산': np.random.randint(1_000_000, 200_000_000, 50),  # 예산 (1백만 ~ 2억 달러)
#     '평점': np.random.uniform(1, 10, 50)  # 평점 (1 ~ 10)
# }

# # DataFrame 생성
# movie_data = pd.DataFrame(data)

# movie_data.to_csv('movie_data.csv', index=False, encoding='utf-8')

# 문제 4: 영화 평점 예측
# 주어진 영화 데이터셋을 사용하여, 영화의 평점을 예측하는 모델을 만드세요.

# 주어진 데이터셋:
# 영화의 특성(장르, 감독, 출연 배우 등)을 사용하여 영화 평점을 예측하는 문제입니다.
# 과제:
# 1. 영화 데이터셋을 로드하고, 영화의 특성(예: 장르, 감독 등)과 평점을 추출하세요.
# 2. 훈련 데이터와 테스트 데이터로 나누세요.
# 3. 랜덤 포레스트 회귀(Random Forest Regressor) 모델을 사용하여 훈련시키세요.
# 4. 테스트 데이터셋을 사용하여 평점을 예측하고, 예측값과 실제 평점을 비교하여 정확도를 평가하세요.

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 1. 영화 데이터셋을 로드하고, 영화의 특성(예: 장르, 감독 등)과 평점을 추출하세요.
movie_data = pd.read_csv("C:/Users/권유림/Desktop/aiStudy/movie_data.csv")
label_encoders = {}
for col in ['장르', '감독', '출연 배우']:
    le = LabelEncoder()
    movie_data[col] = le.fit_transform(movie_data[col])
    label_encoders[col] = le  # 나중에 inverse_transform을 위해 저장

# 2. 훈련 데이터와 테스트 데이터로 나누세요.
X = movie_data.drop(columns=["평점"])
y = movie_data["평점"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. 랜덤 포레스트 회귀(Random Forest Regressor) 모델을 사용하여 훈련시키세요.
#일단 정규화 부터!!!!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#훈련
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 4. 테스트 데이터셋을 사용하여 평점을 예측하고, 예측값과 실제 평점을 비교하여 정확도를 평가하세요.
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f"평균 제곱 오차 (MSE): {mse:.4f}")
