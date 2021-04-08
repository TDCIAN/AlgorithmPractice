"""
대표적인 정렬1: 버블 정렬(bubble sort)
0. 알고리즘 연습 방법
- 알고리즘을 잘 작성하기 위해서는 잘 작성된 알고리즘을 이해하고, 스스로 만들어봐야 함
    - 모사! 그림을 잘 그리기 위해서는 잘 그린 그림을 모방하는 것부터 시작

* 알고리즘 연습 방법(순서)
    1. 연습장과 펜을 준비하자.
    2. 알고리즘 문제를 읽고 분석한 후에,
    3. 간단하게 테스트용으로 매우 간단한 경우부터 복잡한 경우까지 순서대로 생각해보면서, 연습장과 펜을 이용하여 알고리즘을 생각해본다.
    4. 가능한 알고리즘이 보인다면, 구현할 알고리즘을 세부 항목으로 나누고, 문장으로 세부 항목을 나누어서 적어본다.
    5. 코드화하기 위해, 데이터 구조 또는 사용할 변수를 정리하고,
    6. 각 문장을 코드 레벨로 적는다.
    7. 데이터 구조 또는 사용할 변수가 코드에 따라 어떻게 변하는지를 손으로 적으면서, 임의 데이터로 코드가 정상 동작하는지를
       연습장과 펜으로 검증한다.

1. 정렬(sorting)이란?
- 정렬(sorting): 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
- 정렬은 프로그램 작성시 빈번하게 필요로 함
- 다양한 알고리즘이 고안되었으며, 알고리즘 학습의 필수
    - 다양한 정렬 알고리즘 이해를 통해, 동일한 문제에 대해 다양한 알고리즘이 고안될 수 있음을 이해하고,
      각 알고리즘간 성능 비교를 통해, 알고리즘 성능 분석에 대해서도 이해할 수 있음

2. 버블 정렬(bubble sort)란?
- 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘
- 수도코드
  for index in range(데이터길이 - 1):
      for index2 in range(데이터길이 - index - 1):
          if 앞데이터 > 뒤데이터:
              swap(앞데이터, 뒤데이터)

    * 연습장 작성 예시
    1. for num in range(len(data_list)) 반복
    2. swap = 0 (교환이 되었는지를 확인하는 변수를 두자)
    3. 반복문 안에서, for index in range(len(data_list) - num - 1)n - 1번 반복해야 하므로
    4. 반복문 안의 반복문 안에서, if data_list[index] > data_list[index + 1]이면
    5. data_list[index], data_list[index + 1] = data_list[index + 1], data_list[index]
    6. swap += 1
    7. 반복문 안에서 if swap == 0 이면, break 끝

5. 알고리즘 분석
- 반복문이 두 개 -> O(n^2)
    - 최악의 경우 n*(n-1)/2
- 완전 정렬이 되어 있는 상태라면 최선은 O(n)
"""

def bubblesort(data):
    for index in range(len(data) - 1):
        swap = True
        print("len(data): {}, index: {}, 그래서 만들어진 레인지: {}".format(len(data), index, len(data) - index - 1))
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break
    return data

import random

data_list = random.sample(range(100), 50)
print(data_list)
print("버블정렬: ",bubblesort(data_list))