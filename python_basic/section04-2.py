# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am a boy"
str2 = "Nice man"
str3 = ' '

print(len(str1), len(str2), len(str3))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tab \tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
"""
문자열 
멀티라인 
테스트
""" 
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = "abc"
str_o3 = "def"
str_o4 = "Niceman"
print(str_o1 * 100)
print(str_o2 + str_o3)
print('a' in str_o4)
print('z' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수
a = "Niceman"
b = "orange"
print(a.islower())
print(b.islower())
print(a.endswith('e'))
print(b.endswith('e'))
print(a.capitalize())
print(b.capitalize())
print(a.replace('Nice', 'good'))
print(list(reversed(b)))

a = "Niceman"
b = "orange"
print(a[0:3])
print(a[0:len(a)])
print(a[0:len(a)-1])
print(a[0:])
print(a[:])
print(a[:4])
print(b[::-1]) # 처음부터 끝까지 나오는데 역순으로
print(b[0:4:2])
print(b[1:-2])
print(b[2:-1])
print(b[2:-2])
print(b[::-1])

