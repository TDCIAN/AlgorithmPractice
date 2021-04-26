"""
멘토세션3

01. 탐색 알고리즘
- 자료구조에서 원하는 자료를 찾아내는 것을 탐색이라고 한다.
- 선형 자료구조
    - 효율적인 탐색: O(n)보다 빠른 탐색
    - 정렬/비정렬 상태에 따른 탐색
    - O(nlogn) 이상의 시간 복잡도를 가진 알고리즘은 실제론 쓰기 어렵다(너무 느려서)

- 비선형 자료구조
    - 탐색 그 자체가 난제
    - 회로가 있는 경우 무한 루프 방지
    - 효율적인 탐색(사용 가능한 수준)
        - O(nlogn) 이상의 시간 복잡도를 가진 알고리즘은 실제론 쓰기 어렵다(너무 느려서)
    - 올바른 알고리즘을 선택하여 사용

- 선형 자료구조의 효율적인 탐색 전략들
    - 전략1: 단순한 O(N) 순차 탐색
    - 전략2: 해싱을 이용한 O(1) 탐색
        - set(), dict() 등을 활용
        - 공간복잡도는 올라감
    - 전략3: 정렬을 이용한 O(logN) 탐색
        - sort()를 이용한 정렬 이후 이진 탐색 -> sort()는 NlogN의 시간복잡도를 가진다
    - 전략4: 비선형 자료구조로 변환(Heap, BST 등) -> Heap과 BST 모두 O(logN)의 시간복잡도
        - 탐색 목적에 맞는 특정 자료구조 선택
"""
import random
data = [x for x in range(100000)]
query = [x for x in range(100000)]
random.shuffle(data)

# 전략1 - 단순한 O(n) 순차 탐색
# O(m*n)
for q in query: # O(m)
    res = q in data # O(n)

# 전략2 - 해싱을 이용한 O(1) 탐색 - 추가 메모리 사용 O(n + m)
data_set = set(data) # O(n)
for q in query: # O(m)
    res = q in data_set # O(1)

# 전략3 - 정렬을 이용한 O(logN) 탐색 - 추가 메모리 O(n)
data_sort = sorted(data) # O(nlogn)
for q in query: # O(mlogn)
    res = bisect.bisect(data_sort, q) # O(logn)

# 전략 - 비선형 자료구조로 변환 (Heap, BST, ...)
# 최소값을 하나씩 반환하는 알고리즘
# Navie method(나이브하게 짰을 때)
data_ = data.copy()
while data_: # O(n^2)
    val = min(data_) # O(n)
    data_.remove(val)

# Sorting
data_sorted = sorted(data, reverse = True) # O(nlogn)
while data_sorted: # O(n)
    val = data_sorted[-1] # O(1)
    del data_sorted[-1]

# Heap으로 만들기
import heapq
data_heap = data.copy()
heapq.heapify(data_heap) # O(nlogn)
while data_heap: # O(nlogn)
    val = heapq.heappop(data_heap) # O(logn)

