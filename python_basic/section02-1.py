# Section02-1
# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019','02','19',sep='-')
print('niceman','google.com',sep='@')

# end 옵션 사용 - 끝 부분을 다음 라인과 연결
print('Welcome To', end=' ')
print('the black paradise', end=' ')
print('piano notes')
print('guitar')

print()

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a = 'You', b = 'Me'))

# %s -> 문자, %d -> 정수, %f -> 실수
print("%s's favorite number is %d" % ('Jeongmin', 7))

# 다섯자리 숫자의 정수 
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a = 776, b = 6534.123))

"""
참고: Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
"""

print("'You'")
print('\'You\'')
print('"You"')
print("""'You'""")
print('\\you\\\n')
print('\t\t\ttest') # 탭 키임

