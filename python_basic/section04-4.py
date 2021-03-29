# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary): 순서 없음, 키는 중복 불가(값은 가능), 수정 가능, 삭제 가능
# Key와 Value로 이루어짐(JSON, MongoDB 등)
# Key를 가지고 Value를 조회를 한다

# 선언 방식
a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 870214, 'name': 'Park'}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

# 출력
print(a['name'])
print(a.get('name')) # get을 쓰는 것이 더 안전하다 
print(a.get('address'))
print(c['arr'])
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = ((1,2,3))
print(a)

# Keys, Values, items
# item은 키와 밸류 전체를 뜻한다
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(2 in b)
print(1 in b)
print('Hello Python' in b)
print('name' in a)

# 집합(Sets) (순서 X, 중복 X)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c) # {1, 4, 5, 6} -> 중복 없음

t = tuple(b)
print(t) # (1, 2, 3, 4) -> 튜플로 변환됨

l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2)) # {4, 5, 6}
print(s1 & s2) # {4, 5, 6}

# 합집합
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합
print(s1 - s2) # {1, 2, 3}
print(s1.difference(s2)) # {1, 2, 3}

# 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
s3.add(7) # 중복은 허용하지 않는다

print(s3) # {7, 8, 10, 15, 18}

s3.remove(15)
print(s3) # {7, 8, 10, 18}

print(type(s3)) # <class 'set'>