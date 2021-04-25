"""
문제 제목: 피보나치 수 - 백준 2747번
문제 난이도: 하
문제 유형: 재귀 함수
추천 풀이 시간: 15분

문제 풀이 핵심 아이디어
1. 피보나치 수열의 점화식을 세웁니다.
    F_0 = 0, F_1 = 1
    F_n = F_n-1 + F_n-2 (n >= 2)

2. 재귀 함수를 이용해 문제를 풀 수 있는지 검토해야 합니다.
3. 문제에서 N은 최대 45입니다.

피보나치 수열 -> 재귀적 구현의 한계 -> 재귀 함수로 풀면 안 된다
"""
n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)

"""
문제 제목: Z - 백준 1074번
문제 난이도: 중
문제 유형: 재귀 함수
추천 풀이 시간: 40분
"""
def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    solve(n / 2, x, y)
    solve(n / 2, x, y + n / 2)
    solve(n / 2, x + n / 2, y)
    solve(n / 2, x + n / 2, y + n / 2)

result = 0
N, X, Y = map(int, input().split(' '))
solve(2 ** N, 0, 0)


"""
문제 제목: 0 만들기 - 백준 7490번
문제 난이도: 중
문제 유형: 재귀 함수
추천 풀이 시간: 40분

문제 풀이 핵심 아이디어
1. 자연수 N의 범위(3 <= N <= 9)가 매우 한정적이므로 완전 탐색으로 문제를 해결할 수 있습니다.
2. 수의 리스트와 연산자 리스트를 분리하여 모든 경우의 수를 계산합니다.
3. 가능한 모든 경우를 고려하여 연산자 리스트를 만드는 것이 관건입니다(재귀함수 이용).
4. 파이썬의 eval() 함수를 이용하여 문자열 형태의 표현식을 계산할 수 있습니다.
"""

import copy

def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n - 1)

    integers = [i for i in range(1, n + 1)]

    for operators in operators_list:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()
    