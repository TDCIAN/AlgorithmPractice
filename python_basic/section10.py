# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# liner: 코드 스타일, 문법 체크

# (1) SyntaxError: 잘못된 문법
# print('Test) -> SyntaxError: EOL while scanning string literal (따옴표 없어서)
# if True -> SyntaxError: invalid syntax (괄호 없어서)
#     pass 

# (2) NameError: 참조변수 없을 때
a = 10
b = 15
# print(c) -> NameError: name 'c' is not defined (c는 아직 정의 안 됨)

# (3) ZeroDivisionError: 0 나누기 에러
# print(10 / 0) -> ZeroDivisionError: division by zero (0으로 나눠서)

# IndexError: 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3]) -> IndexError: list index out of range (2까지 밖에 없어서)

# KeyError
dic = {
    'name': 'Kim',
    'Age': 33,
    'City': 'Seoul'
}

# print(dic['hobby']) -> KeyError: 'hobby' (hobby라는 키는 없음)
print(dic.get('hobby')) # 얘는 그냥 None이라고 뜸

# AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month()) -> AttributeError: module 'time' has no attribute 'month' (month라는 메소드는 없음)

# ValueError: 참조 값이 없을 때 발생
x = [1, 5, 9]

# x.remove(10) -> ValueError: list.remove(x): x not in list
# x.index(20) -> ValueError: 20 is not in list
print("1의 인덱스 ", x.index(1))

# FileNotFoundError
# f = open('test.txt', 'r') -> FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# TypeError
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) -> TypeError: can only concatenate list (not "tuple") to list
# print(x + z) -> TypeError: can only concatenate list (not "str") to list
print(x + list(y)) # 이러면 괜찮음

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩을 하고
# 그 후 런타임 예외 발생시 예외 처리 코딩을 권장함(EAFP 코딩 스타일이라 함)

# 예외 처리 기본
# try: 에러가 발생할 가능성이 있는 코드 실행
# except: 에러명1
# except: 에러명2
# else: 에러가 발생하지 않았을 경우 실행
# finally: 항상 실행

# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    # z = 'Cho'
    x = name.index(z)
    print('Found {} in name list!'.format(z, x+1))
except ValueError:
    print('Not found it! - Occured ValueError!')
else: # try문이 정상적으로 실행 됐을때 실행 되는 부분
    print('Ok! else!')
finally:
    print('finally ok!')

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('Ok Finally!')


# 예제5
try:
    # z = 'Kim'
    z = 'Cho'
    x = name.index(z)
    print('Found {} in name list!'.format(z, x+1))
except ValueError:
    print('Not found it! - Occured ValueError!')
except IndexError:
    print('Not found it! - Occured IndexError!')
except Exception:
    print('Not found it! - Occured Exception!')
else: # try문이 정상적으로 실행 됐을때 실행 되는 부분
    print('Ok! else!')
finally:
    print('finally ok!')


# 예제6
# 예외 발생: raise
# raise 키워드로 예외 직접 발생
try:
    # a = 'Kim'
    a = 'Kimb'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('Ok!')
