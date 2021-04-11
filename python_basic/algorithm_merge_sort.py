"""
1. 병합 정렬 (merge sort)
- 재귀 용법을 활용한 정렬 알고리즘
    1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
    2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
    3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

2. 알고리즘 이해
- 데이터가 네 개 일때(데이터 갯수에 따라 복잡도가 떨어지는 것은 아니므로, 네 개로 바로 로직을 이해해보자)
    - 예: data_list = [1, 9, 3, 2]
        - 먼저 [1, 9], [3, 2]로 나누고
        - 다시 앞 부분은 [1], [9]로 나누고
        - 다시 정렬해서 합친다. [1, 9]
        - 다음 [3, 2]는 [3], [2]로 나누고
        - 다시 정렬해서 합친다 [2, 3]
        - 이제 [1, 9]와 [2, 3]을 합친다.
            - 1 < 2 이니 [1]
            - 9 > 2 이니  [1, 2]
            - 9 > 3 이니 [1, 2, 3]
            - 9밖에 없으니 [1, 2, 3, 9]

3. 알고리즘 구현
- mergesplit 함수 만들기
    - 만약 리스트 갯수가 한개이면 해당 값 리턴
    - 그렇지 않으면, 리스트를 앞뒤, 두 개로 나누기
    - left = mergesplit(앞)
    - right = mergesplit(뒤)
    - merge(left, right)

- merge 함수 만들기
    - 리스트 변수 하나 만들기 (sorted)
    - left_index, right_index = 0
    - while left_index < len(left) or right_index < len(right):
        - 만약 left_index나 right_index가 이미 left 또는 right 리스트를 다 순회했다면,
          그 반대쪽 데이터를 그대로 넣고, 해당 인덱스 1 증가
        if left[left_index] < right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1
"""

# 데이터리스트가 있을 때 리스트를 앞 뒤로 짜르는 코드 작성하기
def split(data):
    medium = int(len(data) / 2) # int로 형변환 하면 결과는 내림으로 나오네
    left = data[:medium]
    right = data[medium:]
    print("미디엄: ",medium) # 미디엄:  3
    print(left, right) # [3, 4, 1] [3, 2, 5, 9]

data_list = [3, 4, 1, 3, 2, 5, 9]

"""
mergesplit 함수 만들기
- 만약 리스트 갯수가 한 개이면 해당 값 리턴
- 그렇지 않으면, 리스트를 앞뒤, 두 개로 나누기
- left = mergesplit(앞)
- right = mergesplit(뒤)
- merge(left, right)
"""

"""
merge 함수 만들기
- 목표: left와 right의 리스트 데이터를 정렬해서 sorted_list 라는 이름으로 return 하기
- left와 right는 이미 정렬된 상태 또는 데이터가 하나임
"""
def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case1: left / right 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2: left만 남아있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3: right만 남아있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def mergesplit(data):
    if len(data) <= 1:
        return data 
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

import random

data_list = random.sample(range(100), 10)

print("병합 정렬 결과물: ", mergesplit(data_list))