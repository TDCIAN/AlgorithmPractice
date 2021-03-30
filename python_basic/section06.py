# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
# code

# 함수 호출
# 함수명(parameter)
# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello ", world)

hello("Python!")
hello(7777)

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!")
print(str)

# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print("밸1: ",val1," 밸2:", val2, "밸3: ", val3)

# 예제4-1(리스트 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 예제4-2(튜플 타입 반환)
def func_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)

tp = func_mul3(100)
print(tp, type(tp))


# 예제4
# *args, #kwargs

# *args - 매개변수가 몇 개가 넘어올지 모를 때, 매개변수가 넘어오는 것에 따라 함수의 작동이 달라질 때
def args_func(*args): # *가 하나일 때는 튜플로, *가 두 개일 때는 딕셔너리로 받는다
    # for i, v in enumerate(args):
    for i, v in enumerate(range(10)):
        print(i, v)
    # print(args)
    # for t in args:
    #     print(t)

# args_func('kim')
args_func('kim', 'Park', 'Lee')


# kwargs (kw는 keyword의 줄임말)
def kwargs_func(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1 = "Kim", name2 = "Park", name3 = "Lee")

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20) # 10 20 () {}
example_mul(10, 20, 'Park', 'Kim') # 10 20 ('Park', 'kim') {}
example_mul(10, 20, 'Park', 'Kim', age1 = 24, age2 = 35)

# 중첩함수(클로저)
def nested_func(num):
    def func_infunc(num):
        print('>>>',num)
    print("in function")
    func_infunc(num + 10000)

nested_func(10000)

# 예제 6
def func_mul4(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul4(5))

# 람다식
# 람다식 - 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10

var_func = mul_10
print(var_func) # <function mul_10 at 0x7f987242cee0>
print(type(var_func)) # <class 'function'>
print(var_func(10)) # 100

lambda_mul_10 = lambda num: num * 10
# print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 300))