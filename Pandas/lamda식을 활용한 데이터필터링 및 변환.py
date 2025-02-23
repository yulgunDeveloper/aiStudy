# 문제 3: Lambda식을 활용한 데이터 필터링 및 변환
# 5. 최종 결과를 "processed_students.csv" 파일로 저장하세요.

# 📌 데이터
# 이름(name)	나이(age)	도시(city)	점수(score)
# 철수	25	서울	90
# 영희	23	부산	85
# 민수	30	대구	88
# 지민	27	서울	95
# 수현	22	부산	80

# 1. 데이터를 DataFrame으로 생성하세요.

import pandas as pd

data = {
    "이름(name)":["철수", "영희", "민수", "지민", "수현"],
    "나이(age)":[25, 23, 30, 27, 22],
    "도시(city)": ["서울", "부산", "대구", "서울", "부산"],
    "점수(score)":[90, 85, 88, 95, 80]
}

df = pd.DataFrame(data)

# 2. 점수(score)가 85 이상인 학생만 필터링하세요. (lambda 사용)

filter_score = df.loc[df['점수(score)'].apply(lambda x:x >= 85)]
print(filter_score)

# 3. 이름(name) 컬럼의 값을 모두 대문자로 변환하세요. (lambda 사용)

df["이름(name)"] = df["이름(name)"].apply(lambda x:x.upper())

# 4. **나이(age)가 25 이상이면 "성인", 
# 아니면 "미성년"**이라는 새로운 컬럼 **"구분(category)"**을 추가하세요. (lambda 사용)

# df["구분(category)"] = df['나이(age)'].apply(lambda x : x >= 25)
df["구분(category)"] = df["나이(age)"].apply(lambda x: "성인" if x >= 25 else "미성년")
print(df)


# 5. 최종 결과를 "processed_students.csv" 파일로 저장하세요.
df.to_csv("processed_students.csv", index=False)