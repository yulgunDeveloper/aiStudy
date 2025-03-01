# import pandas as pd

# # 데이터 생성 (결측치 & 중복 포함)
# data = {
#     "이름": ["김철수", "이영희", "박민수", "최지우", "김철수", "한예린", "이영희", "정우성", "신민아", None],
#     "국어": [90, 85, 88, 92, 87, 78, 85, 91, None, 80],
#     "영어": [85, 80, 82, None, 89, 74, 80, 95, 88, 76],
#     "수학": [88, 82, None, 96, 90, 79, 82, 92, 85, 75],
#     "과학": [92, 88, 85, 94, 89, None, 88, 93, 90, 82],
#     "사회": [87, 83, 80, 90, 85, 77, None, 89, 84, 79],
#     "성별": ["남", "여", "남", "여", "남", "여", "여", "남", "여", "여"]
# }

# # DataFrame 생성
# df = pd.DataFrame(data)

# # CSV 파일 저장
# df.to_csv("sample_data2.csv", index=False, encoding="utf-8-sig")

# print("📂 'sample_data2.csv' 파일이 생성되었습니다!")

# 🔹 [문제 2] 데이터 전처리
# 💡 데이터 정리를 위해 다음 전처리 과정을 수행하세요.
# ✅ 추가 요구사항:
# 1. 결측치가 포함된 행을 제거하세요.
# 2. 특정 컬럼에서 중복된 데이터를 제거하세요.
# 3. 새로운 컬럼(예: ‘총점’ 또는 ‘평균’)을 추가하세요.

import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("sample_data2.csv")

# 결측치가 포함된 행 제거
df_cleaned = df.dropna().copy() # 원본과 분리

# 중목 데이터 제거
print("제거 전:",df)
df_cleaned = df_cleaned.drop_duplicates(subset=["이름"])
print(df)

# 새로운 칼럼 총점 및 평균 추가
df_cleaned["총점"] = df_cleaned["국어"] + df_cleaned["영어"] + df_cleaned["수학"] + df_cleaned["과학"] + df_cleaned["사회"]
df_cleaned["평균"] = df_cleaned["총점"] / 5
print(df_cleaned)