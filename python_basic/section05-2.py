# # Section05-2
# # 파이썬 흐름제어(반복문)
# # 반복문 실습

# # 코딩의 핵심 -> 조건 해결 중요

# # 기본 반복문: for, while 

# x1 = 1
# while x1 < 11:
#     print("x1 is :", x1)
#     x1 += 1

# for y2 in range(10):
#     print("y2 is :", y2)

# for z3 in range(1, 11):
#     print("z3 is :", z3)

# # 1 ~ 100 합
# sum1 = 0
# cnt1 = 0

# while cnt1 <= 100:
#     sum1 += cnt1
#     cnt1 += 1

# print('1 ~ 100: ', sum1) # 5050
# print('1 ~ 100: ', sum(range(1, 101))) # 5050
# print('1 ~ 100: ', sum(range(1, 101, 2))) # 2500

# # 시퀀스(순서가 있는) 자료형 반복
# # 문자열, 리스트, 튜플, 집합, 사전
# # iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

# for name in names:
#     print("name: ", name)

# word = "dreams"
# for s in word:
#     print("Word: ", s)

# my_info = {
#     "name" : "Kim",
#     "age" : 33,
#     "city" : "Seoul"
# }

# # 기본 값은 키
# for kkey in my_info:
#     print("my_info - key: ", kkey)

# # 값
# for vvalue in my_info.values():
#     print("my_info - values: ", vvalue)

# # 키
# for ggey in my_info.keys():
#     print("my_info - keys: ", ggey)

# # 키 and 값
# for k, v in my_info.items():
#     print("my_info - key & value: ", k, "is", v)

# name = "KennRY"

# for n in name:
#     if n.isupper():
#         print(n.lower())
#     else:
#         print(n.upper())

# # break - 조건이 맞으면 반복문을 탈출할 수 있게 한다
# numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]

# for num in numbers:
#     if num == 33:
#         print("found: 33!")
#         break
#     else:
#         print("not found: 33!")

# # for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# for num in numbers:
#     if num == 33:
#         print("found: 33!")
#         break
#     else:
#         print("not found: 33!")
# else:
#     print("Not found 33...")

# # continue - 스킵함
# lt = ["1", 2, 5, True, 4.3, complex(4)]

# for v in lt:
#     if type(v) is float:
#         continue
#     print("타입: ", type(v))

# name = "Niceman"
# print(reversed(name)) # <reversed object at 0x7fe0d8a3b400>
# print(list(reversed(name))) # ['n', 'a', 'm', 'e', 'c', 'i', 'N']
# print(tuple(reversed(name))) # ('n', 'a', 'm', 'e', 'c', 'i', 'N')

