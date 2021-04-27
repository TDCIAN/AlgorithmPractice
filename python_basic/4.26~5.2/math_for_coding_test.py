"""
코딩테스트에 나오는 수학
- 코딩테스트에 나오는 수학은 정수론 그리고 기하가 대표적입니다.
- 코딩테스트 내의 기하는 피타고라스 정리를 활용한 점 사이의 거리 등 쉽게 알 수 있는 내용이거나
  CCW, 컨벡스헐, 좌표기하 등 내용이 어려워 난이도 격차가 꽤 있는 분야입니다.
- 강의에서는 다음과 같은 주제를 다룹니다.
    - GCD / LCM
    - 소수 체크와 소인수분해
    - 에라토스테네스의 체 활용
    - 거듭제곱 연산

GCD와 LCM
- Greatest Common Divider와 Least Common Multiple은 가장 많이 나오는 유형 중 하나입니다.
- 최대공약수 / 최소공배수를 묻는 문제의 90% 이상은 이 알고리즘을 사용하니 알아둬야 합니다.
- 최소공배수의 경우에는 다음과 같은 식으로 풀 수 있으므로 최대공약수만 알면 됩니다.
    - LCM(a,b) = a*b / GCD(a,b)
- 총 3개의 방법을 소개합니다.
    - 단순 반복문으로 하는 방법
    - 유클리드 호제법을 이용한 방법
        - 유클리드 호제법의 경우는 다음 성질을 활용한 방법입니다.
            - GCD(a,b) = GCD(b, a%b)
    - 라이브러리를 사용하는 방법
"""
# 방법1: 단순하게 반복문 사용 -> O(n)
def gcd_naive(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0: 
            return i

# 방법2-1: 유클리드호제법을 이용한 방법 -> 1번보다 훨씬 빠름(10분의 1정도)
def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

# 방법2-2: 반복문으로 변경 -> 2번보다 약간 빠름
def gcd2(a, b):
    while a%b != 0: a,b = b,a%b
    return b

# 방법3: math의 gcd 사용하기 -> 제일 빠름
import math
math.gcd(1,2)

print("나이브: ",gcd_naive(6, 24))
print("유클리드호제: ",gcd(6, 24))
print("유클리드호제 반복문 변경: ",gcd2(6, 24))
print("math의 gcd: ",math.gcd(6, 24))

# LCM은 GCD를 활용하여 계산하자
# 만약 Python이 아닌 다른 언어의 경우 int overflow가 발생할 수 있으니
# a/gcd(a,b)*b 순서로 하는 것을 추천합니다.
def lcm(a, b):
    return a*b/gcd(a,b)

"""
소수 체크와 소인수 분해
- 소수 체크와 소인수 분해도 꽤 많이 나오는 유형입니다. 소수 체크는 반복문으로 진행하면 되고,
  소인수분해의 경우는 조금의 트릭으로 진행하면 됩니다.
- 두 알고리즘 모두 시간복잡도는 O(루트N)입니다.
"""
# 소수 체크 기본
# (prime_check말고 isPrime 등의 관용적인 함수 명을 사용)
def prime_check(N):
    for i in range(2, N):
        if N%i == 0: return False
        if i*i > N: break
    return True

# 소인수분해 기본
def prime_factorization(N):
    p, fac = 2, []
    while p**2 <= N:
        if N%p == 0:
            N //= p
            fac.append(p)
        else:
            p += 1
    if N > 1: fac.append(N)
    return fac

print(prime_factorization(12345))

# 이런 알고리즘이 단 한 번 사용하거나 빠르게 체크할 때는 좋지만 여러 쿼리를 묻는 문제 등의 경우에는 시간복잡도가 꽤 큽니다.
# 이런 문제를 해결하기 위해 소수 리스트를 미리 만드는 방법이 있는데 이것이 에라토스테네스의 체입니다.
# 에라토스테네스의 체를 활용한 소수 리스트 구하기
def era_prime(N):
    A, p = [0 for _ in range(N+1)], []
    for i in range(2, N):
        if A[i] == 0:
            p.append(i)
        else:
            continue
        for j in range(i**2, N, i):
            A[j] = 1
    return p

print("에라프라임: ",era_prime(100))
# 이런 리스트를 만들면 소인수분해도 다음과 같이 할 수 있습니다.

# 소수 리스트가 있는 경우 소인수분해
# 소수 리스트의 크기는 sqrt(N)보다 커야함
def prime_factorization_2(N, p):
    fac = []
    for i in p:
        if N == 1 or N > i*i:
            break
        while N%i == 0:
            fac.append(i)
            N //= i
    return fac

# 활용 1: 소인수의 개수
def era_factor_count(N):
    A = [0 for _ in range(N+1)]
    for i in range(2, N):
        for j in range(i, N, i):
            A[j] += 1
    return A

# 활용 2: 소인수의 합
def era_factor_sum(N):
    A = [0 for _ in range(N+1)]
    for i in range(2, N):
        for j in range(i, N, i):
            A[j] += i
    return A

# 활용 3: 소인수분해 하기
def era_factorization(N):
    A = [0 for _ in range(N+1)]
    for i in range(2, N):
        if A[i] == 1:
            continue
        for j in range(i, N, i):
            A[j] = i
    return A

# 소인수분해하는 방법
A = era_factorization(100)
print("A값: ",A)
N = 84
while A[N] != 0:
    print("A[N]값: ", A[N])
    N //= A[N]

"""
빠른 거듭제곱과 모듈러
- Python에서는 크게 많이 고민할 부분은 아니지만 거듭제곱 연산을 해야할 때가 있습니다.
- 이런 거듭제곱을 순수하게 반복문으로 진행하는 것이 아니라 효율적인 방법을 살펴봅시다
"""
def pow_advanced(a, b, mod):
    ret = 1
    while b > 0:
        if b % 2: ret = ret * a % mod
        a, b = a * a % mod, b//2
    return ret

print("파우_어드밴스드: ",pow_advanced(3, 1000000, 10000007))
print("파우함수: ",pow(3, 1000000, 10000007))
print("쌩 곱셈: ", 3**1000000%10000007, %time)


