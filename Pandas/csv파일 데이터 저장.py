# 문제 1: CSV 파일로부터 데이터 불러오기 및 저장
# 아래와 같은 데이터를 포함하는 CSV 파일을 생성하고, 이를 pandas를 사용하여 불러옵니다.

# 이름, 나이, 도시, 점수
# 철수, 25, 서울, 90
# 영희, 23, 부산, 85
# 민수, 30, 대구, 88
# CSV 파일을 불러온 후, **'나이'**가 25 이상인 사람들의 데이터만 출력하고,
# 그 결과를 **filtered_data.csv**라는 이름으로 저장하세요.

# 힌트:
# pd.read_csv()로 파일을 읽어옵니다.
# df.to_csv()로 결과를 저장합니다.

import pandas as pd

data = {
    "이름":["철수", "영희", "민수"],
    "나이":[25, 23, 30],
    "도시":["서울", "부산", "대구"],
    "점수":[90, 85, 88]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

read_df = pd.read_csv("data.csv")

filter_df = read_df[read_df['나이'] >= 25]
# filter_df = read_df[read_df['나이'].apply(lambda x : x >= 25)]

filter_df.to_csv("filtered_data.csv")