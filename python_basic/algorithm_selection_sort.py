"""
대표적인 정렬3: 선택 정렬 (selection sort)

1. 선택 정렬 (selection sort)란?
- 다음과 같은 순서를 반복하며 정렬하는 알고리즘
    1. 주어진 데이터 중, 최소값을 찾음
    2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
    3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

2. 어떻게 코드로 만들까?
- 데이터가 두 개 일때
    - 예: dataList = [9, 1]
        - data_list[0] > data_list[1] 이므로 data_list[0] 값과 data_list[1] 값을 교환

- 데이터가 세 개 일때
    - 예: data_list = [9, 1, 7]
        - 처음 한 번 실행하면, 1, 9, 7이 됨
        - 두 번째 실행하면 1, 7, 9가 됨
- 데이터가 네 개 일때
    - 예: data_list = [9, 3, 2, 1]
        - 처음 한 번 실행하면, 1, 3, 2, 9가 됨
        - 두 번째 실행하면, 1, 2, 3, 9가 됨
        - 세 번째 실행하면, 변화 없음

3. 알고리즘 구현
for stand in range(len(data_list) - 1):
    lowest = stand
    for num in range(stand + 1, len(data_list)):
        if data_list[lowest] > data_list[num]:
            lowest = num
    data_list[num], data_list[lowest] = data_list[lowest], data_list[num]

"""
# 실제 삽입정렬 코드
def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data

import random
data_list = random.sample(range(100), 10)

print(selection_sort(data_list))
