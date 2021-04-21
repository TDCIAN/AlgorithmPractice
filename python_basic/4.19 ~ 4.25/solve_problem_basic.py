"""
기본 자료구조 - 01. 기초 문제풀이
"""

"""
문제 제목: 음계 - 백준 2920번
문제 난이도: 하(Easy)
문제 유형: 배열, 구현
추천 풀이 시간: 15분
"""
a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i - 1]:
        descending = False
    elif a[i] < a[i - 1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')


"""
문제 제목: 블랙잭 - 백준 2798번
문제 난이도: 하(Easy)
문제 유형: 배열, 완전 탐색
추천 풀이 시간: 20분
"""
n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

count = 0
for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)
