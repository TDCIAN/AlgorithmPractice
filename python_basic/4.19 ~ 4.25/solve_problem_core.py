"""
기본 자료구조 - 02. 핵심 유형 문제풀이
"""

"""
문제 제목: 스택 수열 - 백준 1874
문제 난이도: 하(Easy)
문제 유형: 스택, 그리디
추천 풀이 시간: 30분
"""

n = int(input())

count = 1
stack = []
result = []

for i in range(1, n + 1): # 데이터 개수만큼 반복
    data = int(input())
    while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else: # 불가능한 경우
        print('No')
        exit(0)

print('\n'.join(result)) # 가능한 경우


"""
문제 제목: 프린터 큐 - 백준 1966번
문제 난이도: 하(Easy)
문제 유형: 큐, 구현, 그리디
추천 풀이 시간: 25분
"""
test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))


"""
문제 제목: 키로거 - 백준 5397번
문제 난이도: 중
문제 유형: 스택, 구현, 그리디
추천 풀이 시간: 40분
"""
test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))


"""
고급 자료구조(핵심 유형 문제 풀이)
"""

"""
문제 제목: SHA-256 - 백준 10930번
문제 난이도: 하
문제 유형: 해시, 구현
추천 풀이 시간: 15분(검색 시간 포함)

문제 풀이 핵심 아이디어
1. hashlib의 sha256 함수를 이용하면 SHA256 해시를 구할 수 있다.
2. hashlib.sha256(문자열의 바이트 객체).hexdigest(): 해시 결과 문자열
"""

import hashlib

input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)


"""
문제 제목: 수 찾기 - 백준 1920번
문제 난이도: 하
문제 유형: 해시, 배열, 구현
추천 풀이 시간: 20분

문제 풀이 핵심 아이디어
1. 특정 정수의 등장 여부만을 간단히 체크하면 된다.
2. Python에서는 dictionary 자료형을 해시처럼 사용할 수 있다.
3. 본 문제는 set 자료형을 이용해 더욱 간단히 풀 수 있다.
"""

n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')


"""
문제 제목: 친구 네트워크 - 백준 4195번
문제 난이도: 중
문제 유형: 해시, 집합, 그래프
추천 풀이 시간: 50분

문제 풀이 핵심 아이디어
1. 해시를 활용한 Union-Find 알고리즘을 이용해 문제를 풀 수 있다.
2. Python에서는 dictionary 자료형을 해시처럼 사용할 수 있다.

합집합 찾기(Union-Find) 알고리즘
- 원소들의 연결 여부를 확인하는 알고리즘
- 더 작은 원소를 부모로 삼도록 설정
"""

# 합집합 찾기 알고리즘
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x

parent = []

for i in range(0, 5):
    parent.append(i)

union(1, 4)
union(2, 4)

for i in range(1, len(parent)):
    print(find(i), end=' ')
        

# 전체 소스코드
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)

    print(number[find(x)])
    