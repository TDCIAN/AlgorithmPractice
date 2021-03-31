# 꼭 알아둬야 할 자료구조: 배열(Array)
# - 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# - 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음

# 1. 배열이 왜 필요할까?
# - 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
# - 같은 종류의 데이터를 순차적으로 저장

# - 배열의 장점
#   - 인덱스를 통해 빠른 접근이 가능
# - 배열의 단점
#   - 추가/삭제가 쉽지 않음

# 2. 파이썬과 C언어의 배열 예제
# # inlcude <stdio.h>
# int main(int, argc, char * argv[])
# {
#   char country[3] = "US";
#   printf("%c%c\n", country[0], country[1]);
#   printf("%s\n", country);
#   return 0;
# }

country = 'US'
print(country)

country = country + 'A'
print(country)

# 3. 파이썬과 배열
# - 파이썬 리스트 활용

# 1차원 배열: 리스트로 구현시
data = [1,2,3,4,5]
print(data)

# 2차원 배열: 리스트로 구현시
data =[[1,2,3],[4,5,6],[7,8,9]]
print(data)
print(data[0][1])
print(data[1][2])

# 3. 프로그래밍 연습
# 위의 2차원 배열에서 9,8,7 순서로 출력해보기
print(data[2][2])
print(data[2][1])
print(data[2][0])

# 연습2: 빈도수 출력하기
dataset = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
target = 5
m_count = 0
for data in dataset:
    if data == target:
        m_count += 1
print("{}는 {}번 들어갔당께".format(target ,m_count))