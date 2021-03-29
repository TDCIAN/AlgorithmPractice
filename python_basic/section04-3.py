# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 -> 순서 있음, 중복 허용, 수정 가능, 삭제 가능
# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2]) # 뒤에서 두번째
print(d[0]+d[1])
print(e[2][1]) # 2번 인덱스(배열형태) 안에서 1번 인덱스에 있는 내용
print(e[-1][-2]) # 역순(-1) 중에서(배열 해당) 끝에서 두 번째

# 슬라이싱
print(d[0:3])
print(e[0:3])
print(e[2][1:3])

# 연산
print(d + e)
print(c * 3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a','b','c']
print(c)

del c[1] # 삭제
print(c)

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7) # 2번 인덱스에 7을 넣겠다
print(y)
y.remove(2) # 2를 삭제한다
print(y)
y.remove(7) # 7을 삭제한다
print(y)
y.pop()
print(y)
ex = [88, 77]
y.append(ex) # 리스트 자체를 추가
print(y)
y.extend(ex) # 리스트 안의 내용을 추가
print(y)

# 삭제: del, remove, pop
# 튜플 -> 순서가 있음, 중복 허용, 수정 불가, 삭제 불가
# 계좌번호 같이 수정될 일이 없고 중요한 내용들이 사용된다
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])
print(d[2:]) # 마지막에 콤마 찍히는 건 규칙임
print(d[2][0:2])

print(c + d)
print(c * 3)
print()
print()

# 튜플 함수
z = (5, 2, 1, 3, 4)
print(z)
print(3 in z)
print(z.index(5)) # z에서 5는 몇 번째 인덱스에 있나?
w = (5, 2, 1, 3, 1)
print(w.count(1)) # w에서 1은 몇 개 있나?

