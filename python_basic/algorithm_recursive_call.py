"""
재귀 용법(recursive call, 재귀 호출)
- 고급 정렬 알고리즘에서 재귀 용법을 사용하므로, 고급 정렬 알고리즘을 익히기 전에 재귀 용법을 먼저 익히기로 합니다.

1. 재귀 용법 (recursive call, 재귀 호출)
- 함수 안에서 동일한 함수를 호출하는 형태
- 여러 알고리즘 작성시 사용되므로, 익숙해져야 함

2. 재귀 용법 이해
- 예제를 풀어보며, 재귀 용법을 이해해보기

예제
- 팩토리얼을 구하는 알고리즘을 Recursive Call을 활용해서 알고리즘 작성하기

예제 - 분석하기
- 간단한 경우부터 생각해보기
    - 2! = 1 * 2
    - 3! = 1 * 2 * 3
    - 4! = 1 * 2 * 3 * 4
- 규칙이 보임: n! = n * (n - 1)!
    1. 함수를 하나 만든다.
    2. 함수(n)은 n > 1이면 return n * 함수(n - 1)
    3. 함수(n)은 n = 1 이면 return n
- 검증 (코드로 검증하지 않고, 직접 간단한 경우부터 대입해서 검증해야 함)
    1. 먼저 2! 부터
        - 함수(2) 이면, 2 > 1이므로 2 * 함수(1)
        - 함수(1) 은 1이므로, return 2 * 1 = 2 -> 맞다!
    2. 먼저 3! 부터
        - 함수(3) 이면, 3 > 1이므로 3 * 함수(2)
        - 함수(2) 는 결국 1번에 의해 2!이므로, return 2 * 1 = 2
        - 3 * 함수(2) = 3 * 2 = 3 * 2 * 1 = 6 -> 맞다!
    3. 먼저 4! 부터
        - 함수(4) 이면, 4 > 1 이므로 4 * 함수(3)
        - 함수(3)은 결국 2번에 의해 3 * 2 * 1 = 6
        - 4 * 함수(3) = 4 * 6 = 24 -> 맞다!

예제 - 시간 복잡도와 공간 복잡도
- factorial(n)은 n - 1번의 factorial() 함수를 호출해서, 곱셈을 함
    - 일종의 n-1번 반복문을 호출한 것과 동일
    - factorial() 함수를 호출할 때마다, 지역변수 n이 생성됨
    - 시간 복잡도 / 공간 복잡도는 O(n-1)이므로, 결국 둘 다 O(n)

3. 재귀 호출의 일반적인 형태
- 일반적인 형태 1
def function(입력):
    if 입력 > 일정값: # 입력이 일정 값 이상이면
        return function(입력 - 1) # 입력보다 작은 값
    else:
        return 일정값, 입력값, 또는 특정값 # 재귀 호출 종료

- 일반적인 형태 2
def function(입력):
    if 입력 <= 일정값: # 입력이 일정 값보다 작으면
        return 일정값, 입력값, 또는 특정값 # 재귀 호출 종료
    function(입력보다 작은 값)
    return 결과값

재귀 호출은 스택의 전형적인 예
- 함수는 내부적으로 스택처럼 관리된다.

참고: 파이썬에서 재귀 함수는 깊이가(한 번에 호출되는) 1000회 이하가 되어야 함
"""
def factorial(n):
    sum = 0
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

print(factorial(3)) # 6

def factorial(num):
    if num <= 1:
        return num
    return num * factorial(num - 1)

print(factorial(4)) # 24


"""
4. 재귀 용법을 활용한 프로그래밍 연습
- 다음 함수를 재귀 함수를 활용해 완성해서 1부터 num까지의 곱이 출력되게 만드세요
"""
def multiple(data):
    if data <= 1:
        return data
    else:
        return data * multiple(data - 1)

print(multiple(10)) # 3628800

# 위 내용을 재귀함수가 아닌 반복문으로 쓰면
def multiple(num):
    return_value = 1
    for index in range(1, num + 1):
        return_value = return_value * index
    return return_value

# 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요
import random
data = random.sample(range(100), 10)
print("랜덤수들: ",data)

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])

print("데이터로 만든 섬리스트: ", sum_list(data))

"""
회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요

참고 - 리스트 슬라이싱
string = 'Dave'
string[-1] --> e
string[0] --> D
string[1:-1] --> av
string[:-1] --> Dav
"""

def palindrome(string):
    if len(string) <= 1: # 앞 뒤가 맞을 때만 안으로 들어와 최종적으로 가운데 있는 문자를 만나니까
        return True 
    
    if string[0] == string[-1]:
        return palindrome(string[1:-1]) # 양 끝을 비교하고 다시 양쪽에서 하나씩 뺀 양쪽을 비교한다
    else:
        return False

print(palindrome('level')) # True
print(palindrome('tomato')) # False

""" 


프로그래밍 연습
1. 정수 n에 대해
2. n이 홀수이면 3 * n + 1을 하고,
3. n이 짝수이면 n을 2로 나눕니다.
4. 이렇게 계속 진행해서 n이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.

예를 들어 n에 3을 넣으면,
3
10 --> 3 * 3 + 1
5 --> 10 / 2
16 --> 3 * 5 + 1
8 --> 16 / 2
4 --> 8 / 2
2 --> 4 / 2
1 --> 2 / 2
이 됩니다.

이렇게 정수 n을 입력받아, 위 알고리즘에 의해 1이 되는 과정을 모두 출력하는 함수를 작성하세요.
"""
def func(num):
    print(num)
    if num == 1:
        return num
    
    if num % 2 == 1:
        return (func((3 * num) + 1))
    else:
        return (func(int(num / 2)))

print("정수 3일 때: ",func(3))
    
"""
프로그래밍 연습
문제: 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
1 + 1 + 1 + 1
1 + 1 + 2
1 + 2 + 1
2 + 1 + 1
2 + 2
1 + 3
3 + 1
정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오

힌트: 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n)이라고 하면,
f(n)은 f(n-1) + f(n-2) + f(n-3)과 동일하다는 패턴 찾기

"""
def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func(data - 1) + func(data - 2) + func(data - 3)

print(func(5)) # 13   

