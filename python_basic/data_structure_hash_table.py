"""
대표적인 데이터 구조6: 해쉬 테이블 (Hash Table)
1. 해쉬 구조
- Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
- 파이썬 딕셔너리(Dictionary) 타입이 해쉬 테이블의 예: Key를 가지고 바로 데이터(Value)를 꺼냄
- 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법)
- 단, 파이썬에서는 해쉬를 별도 구현할 이유가 없음 -> 딕셔너리 타입을 사용하면 됨

2. 알아둘 용어
- 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
- 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
- 해싱 함수(Hashing Fuction): Key에 대한 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
- 해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고,
  이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성 있게 찾을 수 있음
- 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
- 저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음
"""

# 3. 간단한 해쉬 예
# 3.1 hash table 만들기
hash_table_sample = list([0 for i in range(10)]) # list comprehension 사용
print(hash_table_sample) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
hash_table = list([i for i in range(10)])
print(hash_table) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3.2 초간단 해쉬 함수
# 다양한 해쉬 함수 고안 기법이 있는데, 가장 간단한 방식은 Division 법(나누기를 통한 나머지 값을 사용하는 기법)이다.
def hash_func(key):
    return key % 5 # 이렇게 하면 항상 고정된 길이의 해쉬 주소를 얻을 수 있다

print(hash_func(7)) # 7

# 3.3 해쉬 테이블에 저장하기
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

## ord(): 문자의 ASCII(아스키) 코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0])) # 65(A) 68(D) 84(T)
print(ord(data1[0])%5, ord(data2[0])%5, ord(data3[0])%5) # 0 3 4
print( hash_func(ord(data1[0])), hash_func(ord(data2[0])), hash_func(ord(data3[0])) ) # 0 3 4
# 이 때 나눠진 0, 3, 4가 해쉬의 주소가 된다

# 3.3.2 해쉬 테이블에 값을 저장하는 예시
# data:value와 같이 data와 value를 넣으면, 해당 data에 대한 key를 찾아서, 
# 해당 key에 대응하는 해쉬주소에 value를 저장하는 예
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

# 3.4 해쉬 테이블에서 특정 주소의 데이터를 가져오기
storage_data('Andy', '010-1111-1111')
storage_data('Dave', '010-2222-2222')
storage_data('Trump', '010-3333-3333')

# 3.5 실제 데이터를 저장하고 읽기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy')) # 010-1111-1111
print(get_data('Dave')) # 010-2222-2222
print(get_data('Trump')) # 010-3333-3333

"""
4. 자료구조 해쉬 테이블의 장단점과 주요 용도
- 장점
    - 데이터 저장/읽기 속도가 빠르다(검색 속도가 빠르다)
    - 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
- 단점
    - 일반적으로 저장공간이 좀더 많이 필요하다.
    - 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함
- 주요 용도
    - 검색이 많이 필요한 경우
    - 저장, 삭제, 읽기가 빈번한 경우 -> 배열의 경우 모든 경우에 탐색하고 삭제하고 수정해야 해서 오래 걸린다
    - 캐쉬 구현시 (중복 확인이 쉽기 때문)
"""

# 5. 프로그래밍 연습
# 연습1: 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 1. 해쉬 함수 key: % 8
# 2. 해쉬 키 생성: hash(data)
print(hash("Psy")) # 8796273685624645123

hash_table = list([0 for i in range(8)])
print("hash_table: ",hash_table) # [0, 0, 0, 0, 0, 0, 0, 0]
def get_key(data):
    print("겟키:",hash(data))
    return hash(data)

def hash_function(key):
    print("해쉬펑션:",key % 8)
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value
    print("해쉬_어드레스: {}, 밸류: {}".format(hash_address, value))

def read_data(data):
    hash_address = hash_function(get_key(data))
    print("해쉬_테이블[해쉬_어드레스]:", hash_table[hash_address])
    return hash_table[hash_address]

save_data('Dave', '010-1234-1234')
save_data('Andy', '010-2234-2234')

print(read_data('Dave')) # 010-1234-1234

print(hash_table) # [0, 0, 0, 0, 0, 0, 0, '010-2234-2234']

"""
6. 충돌(Collision) 해결 알고리즘 (좋은 해쉬 함수 사용하기)
- 해쉬 테이블의 가장 큰 문제는 충돌(Collision)의 경우입니다. 
  이 문제를 충돌(Collision) 또는 해쉬 충돌(Hash Collision)이라고 부릅니다.
"""

"""
6.1 Chaining 기법
- 개방 해싱 또는 Open Hashing 기법 중 하나: 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
- 충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법
연습2: 연습1의 해쉬 테이블 코드에 Chaining 기법으로 충돌해결 코드를 추가해보기
1. 해쉬 함수: key % 8
2. 해쉬 키 생성: hash(data)
"""
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])): # 여기선 링크드 리스트 대신 어레이로 구현
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        # hash_table[hash_address].append([[index_key, value]])
    else: # 해당 주소에 데이터가 없는 상태라면
        hash_table[hash_address] = [[index_key, value]]

    hash_table[hash_address] = value

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

print("DDD:",hash('DD')%8)
print("DZzz:",hash('DZ')%8)
save_data('DD', '111111')
save_data('DZ', '333333')
print("해시테이블", hash_table)
print("리드_데이터:", read_data('DZ'))

"""
Linear Probing 기법
- 폐쇄 해싱 또는 Close Hashing 기법 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
- 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법
  - 저장공간 활용도를 높이기 위한 기법
"""
# 연습3: 연습1의 해쉬 테이블 코드에 Linear Probing 기법으로 충돌해결 코드를 추가해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)
def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

print(hash('dk')%8)
print(hash('dd')%8)
save_data('dk','11111')
save_data('dd','22222')
print("선형탐사-리드데이터:",read_data('dd'))

"""
6.3 빈번한 충돌을 개선하는 기법
- 해쉬 함수를 재정의 및 해쉬 테이블 저장공간을 확대
"""
# 예시
hash_table = list([None for i in range(16)])

def hash_function(key):
    return key % 16

"""
참고: 해쉬 함수와 키 생성 함수
- 파이썬의 hash() 함수는 실행할 때마다 값이 달라질 수 있음
- 유명한 해시 함수들이 있음: SHA(Secure Hash Algorithm, 안전한 해시 알고리즘)
    - 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용 가능
"""

import hashlib
# SHA-1
data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA-256
data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

# 연습4: 연습2의 Chaining 기법을 적용한 해쉬 테이블 코드에 키 생성 함수를 sha256 해쉬 알고리즘을 사용하도록 변경하기
def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) # 16진수의 문자열을 10진수 정수로 만들어준다

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

print(int(hex_dig, 16))
