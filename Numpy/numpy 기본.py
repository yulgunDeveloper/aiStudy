import numpy as np

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

print("배열의 차원:", arr2.ndim)
print("배열의 크기:", arr2.size)
print("배열의 형태:", arr2.shape)
print("배열의 데이터 타입:", arr2.dtype)

# 리스트처럼 배열 인덱싱 및 슬라이딩이 가능하다.

# 배열 변형
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3) #2행 3열로 변경
print(reshaped_arr)

flattened_arr = reshaped_arr.flatten()  # n차열 배열을 1차원 배열로 변경, 3차원 → 2차원 변환은 reshape()을 사용해야 한다
print(flattened_arr) 


arr = np.array([1, 2, 3, 4, 5])
print("합:", np.sum(arr))        # 합: 15
print("평균:", np.mean(arr))    # 평균: 3.0
print("최소값:", np.min(arr))   # 최소값: 1
print("최대값:", np.max(arr))   # 최대값: 5
print("표준편차:", np.std(arr)) # 표준편차: 1.4142135623730951

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print(arr[1:, 2:])


arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

print(arr[:2, 1:3])

arr = np.array([[ 1,  2,  3,  4,  5],
                [ 6,  7,  8,  9, 10],
                [11, 12, 13, 14, 15]])

print(arr[1:, ::2])

arr1 = np.array([10, 20, 30])

arr1 = np.zeros((2, 3))
arr2 = np.ones((3, 3))
arr3 = np.eye(4)
print("---------")
print(arr1)
print(arr2)
print(arr3)


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

result = np.concatenate((arr1, arr2), axis=0)
print(result)


# 1. 다음 배열에서 10보다 큰 값만 출력하세요.
arr = np.array([[5, 12, 18], 
                [3, 7, 10], 
                [20, 15, 2]])

result = arr[arr > 10]
print(result)


# 2. 다음 배열의 행(row)과 열(column)을 바꿔서 출력하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])


# 행과 열을 바꾸는 방법 (전치)
arr_transposed = arr.T
print(arr_transposed)

# 3. 랜덤 배열 생성 및 평균 계산
# 0과 100 사이의 랜덤 정수로 3x3 배열을 생성하세요.
# 그리고 배열의 평균값을 출력하세요.

arr = np.random.randint(0, 101, size= (3, 3))
print(np.mean(arr))

# 행렬의 곱셈
import numpy as np

A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[5, 6], 
              [7, 8]])

# Dot product 계산
result = np.dot(A, B)  # 또는 A @ B
print("Dot Product 결과:\n", result)

# 4. 랜덤 숫자 배열 생성 후 평균, 최댓값, 최솟값 구하기
# 1) 크기가 4×4인 랜덤 정수 배열을 생성하세요.
# 정수 범위: 1부터 100까지

import numpy as np

arr = np.random.randint(1, 101, size = (4, 4))

# 2) 생성한 배열의 평균값, 최댓값, 최솟값을 구하세요.

print("평균값:", np.mean(arr))
print("최댓값:", np.max(arr))
print("최솟값:", np.min(arr))


# 3) 배열의 각 행별 최댓값과 최솟값도 출력하세요.
row_max = np.max(arr, axis=1)
row_min = np.min(arr, axis=1)

import numpy as np

# 6x6 배열 생성 (1~100 사이의 정수)
arr = np.random.randint(1, 101, size=(6, 6))
mean = np.mean(arr, axis=1)
std = np.std(arr, axis=1)



# 랜덤 숫자 배열 생성 후 평균/최댓값/최솟값 구하기
arr = np.random.randint(1, 101, size=(3, 3))
print(arr)
print("평균 :", np.mean(arr))
print("최댓값 :", np.max(arr))
print("최솟값 :", np.min(arr))
