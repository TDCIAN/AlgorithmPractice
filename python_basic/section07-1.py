# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스: 객체를 인스턴스화할 때 저장된 공간
# 클래스 변수: 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제 1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name): # 클래스를 최초 초기화 할 때 __init__ 메소드를
        self.name = name
        print("초기화", name)
    def user_info_p(self):
        print("Name: ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 예제2
# self의 이해
class SelfTest:
    def function1(): # 클래스 메소드
        print('function1 called!')
    def function2(self): # 인스턴스 메소드
        print('function2 called!')

self_test = SelfTest()
# self_test.function1() -> 이렇게 하면 에러 발생(self가 없어서 누군것인지 모르니까)
SelfTest.function1() # 이렇게 하면 에러 안 난다
self_test.function2() # 이건 self가 있으니까 누구 것인지 알아서 에러 안 난다
# SelfTest.function2() # 이렇게 하면 에러가 발생한다
SelfTest.function2(self_test) # 이렇게 하면 에러 안 난다

# 예제3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.stock_num) # 자기 네임스페이스에 없으면 클래스 네임스페이스에 가서 찾는다


