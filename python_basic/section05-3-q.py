# Section05-3
# 파이썬 흐름제어(제어문)

# 1 ~ 5문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요
q1 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k in q1.keys():
    if k == '가을':
        print(q1[k])

for k, v in q1.items():
    if k == '가을':
        print(v)

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요
q2 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for v in q2.values():
    if v == "사과":
        print("사과 있네 ", v)
        break
else:
    print("사과 없습니다")


# 3. 다음 점수 구간에 맞게 학점을 출력하세요
a = 91
if a >= 81:
    print('A학점')
elif a >= 61:
    print('B학점')
elif a >= 41:
    print('C학점')
elif a >= 21:
    print('D학점')
else:
    print('E학점')

# 4. 다음 세 개의 숫자 중 가장 큰 수를 출력하세요 (if문 사용)
a, b, c = 12, 6, 18
best = a
if b > a:
    best = b
if c > b:
    best = c
print('best: ', best)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1, 3: 남자, 2, 4: 여자)
s = '891022-2473837'
# if s[7] == "1" or s[7] == "3":
#     print("남자네 ", s[7])
# elif s[7] == "2" or s[7] == "4":
#     print("여자네 ", s[7])
# else:
#     print("누구지 ", s[7])

if int(s[7]) % 2 == 1:
    print("남자네 ", s[7])
else:
    print("여자네 ", s[7])

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요
q3 = ["갑", "을", "병", "정"]

for i in q3:
    if i == "정":
        continue
    else:
        print(i, end=' ')

print()
q5 = [x for x in q3 if x != '정']
print("큐빠이브, ",q5)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력하세요.
for n in range(1, 101):
    if n % 2 != 0:
        print(n, end=' ')
print()
q6 = [x for x in range(1, 101) if x % 2 == 1]
print("큐식스 ",q6)
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요
q4 = ["nice", "study", "python", "anaconda", "!"]
for i in q4:
    if len(i) >= 5:
        print(i, end = ' ')

print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for v in q5:
    if v.islower():
        print(v, end=' ')
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로, 대문자는 소문자로 출력하세요
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q6:
    if i.islower():
        print("소문자를 대문자로 ", i.upper(), end =' ')
    elif i.isupper():
        print("대문자를 소문자로 ", i.lower(), end =' ')

print()

# 리스트 컴프리헨션 - 리스트를 쉽게 만드는 기법

# 일반적인 방법
numbers = []
for n in range(1, 101):
    numbers.append(n)
# print(numbers)

# 리스트 컴프리헨션
numbers2 = [x for x in range(1, 101)]
print(numbers2)