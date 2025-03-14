# 문제 2: 데이터 정렬 및 그룹화
# 아래와 같은 데이터를 pandas DataFrame으로 생성합니다.

# 이름, 나이, 도시, 점수
# 철수, 25, 서울, 90
# 영희, 23, 부산, 85
# 민수, 30, 대구, 88
# 짱구, 5, 인천, 79
# 상훈, 24, 부산, 80
# 수진, 28, 서울, 75
# '도시'별로 '점수' 컬럼을 기준으로 내림차순으로 데이터를 정렬하고, 각 도시별로 점수의 평균을 구한 후, 출력하세요.

# 힌트:
# groupby()로 도시별로 그룹화합니다.
# agg()로 평균을 구할 수 있습니다.
# sort_values()로 데이터를 정렬할 수 있습니다.

import pandas as pd

data = {
    "이름":["철수", "영희", "민수", "짱구", "상훈", "수진"],
    "나이":[25, 23, 30, 5, 24, 28],
    "도시":["서울", "부산", "대구", "인천", "부산", "서울"],
    "점수":[90, 85, 88, 79, 80, 75]
}

df = pd.DataFrame(data)
grouped = df.groupby('도시')

# 각 그룹을 점수 기준으로 정렬
sorted_groups = grouped.apply(lambda x: x.sort_values("점수"))

agg_result = grouped['점수'].agg(["mean"])



