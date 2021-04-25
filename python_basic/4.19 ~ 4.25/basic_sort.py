"""
기본 정렬 알고리즘 - 기초 문제풀이
"""

"""
문제 제목: 수 정렬하기 - 백준 2750번
문제 난이도: 하
문제 유형: 정렬
추천 풀이 시간: 15분

문제풀이 핵심 아이디어
1. 데이터의 개수가 1,000개 이하이므로 기본적인 정렬 알고리즘으로 해결할 수 있습니다.
"""
# 1) 선택 정렬 알고리즘으로 문제 해결하기
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

for i in array:
    print(i)

# 2) 파이썬의 기본 정렬 라이브러리로 문제 해결하기
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)


"""
문제 제목: 소트인사이드 - 백준 1427번
문제 난이도: 하
문제 유형: 정렬, 배열
추천 풀이 시간: 25분

문제 풀이 핵심 아이디어
1. 자릿수를 기준으로 정렬하므로 9부터 0까지 차례대로 확인합니다.
2. 각 숫자에 대하여 해당 숫자의 개수를 계산하여 출력합니다.
"""

array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end=' ')


"""
기본 정렬 알고리즘 - 핵심 유형 문제풀이
"""
"""
문제 제목: 나이순 정렬 - 백준 10814
문제 난이도: 하
문제 유형: 정렬
추천 풀이 시간: 15분

문제 풀이 핵심 아이디어
1. (나이, 이름)의 정보를 튜플로 입력 받은 뒤에 나이를 기준으로 정렬합니다.
2. 파이썬의 기본 정렬 라이브러리를 이용하면 됩니다.
3. 나이가 동일한 경우, 먼저 입력된 이름 순서를 따르도록 key 속성을 설정해야 합니다.
"""
n = int(input())

array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

array = sorted(array, key=lambda x: x[0])

for i in array:
    print(i[0], i[1])


"""
문제 제목: 좌표 정렬하기 - 백준 11650번
문제 난이도: 하
문제 유형: 정렬
추천 풀이 시간: 15분

문제 풀이 핵심 아이디어
1. (x 좌표, y 좌표)를 입력 받은 뒤 x 좌표, y 좌표 순서대로 차례대로 오름차순 정렬합니다.
2. 파이썬의 기본 정렬 라이브러리는 기본적으로 튜플의 인덱스 순서대로 오름차순 정렬합니다.
3. 따라서 단순히 기본 정렬 라이브러리를 이용하면 됩니다(key 속성 설정 없이).
"""
n = int(input())

array = []

for _ in range(n):
    x, y = map(int, input().split(' '))
    array.append((x, y))

array = sorted(array)

for i in array:
    print(i[0], i[1])


"""
문제 제목: 수 정렬하기 3 - 백준 10989번
문제 난이도: 하
문제 유형: 정렬
추천 풀이 시간: 20분

문제 풀이 핵심 아이디어
1. 데이터의 개수가 최대 10,000,000개입니다.
2. 시간 복잡도 O(N)의 정렬 알고리즘을 이용해야 합니다.
3. 수의 범위가 1 ~ 10,000이므로 계수 정렬을 이용할 수 있습니다.

계수 정렬(Counting Sort) 알고리즘
- 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법입니다.
- 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정합니다.
- 데이터가 등장한 횟수를 셉니다.
"""
import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

