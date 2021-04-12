"""
탐욕 알고리즘의 이해

1. 탐욕 알고리즘이란?
- Greedy algorithm 또는 탐욕 알고리즘이라고 불리움
- 최적의 해에 가까운 값을 구하기 위해 사용됨
- 여러 경우 중 하나를 결정해야할 때마다, 매순간 최적이라고 생각되는 경우를 선택하는 방식으로 진행해서, 최종적인 값을 구하는 방식
"""

# 2. 탐욕 알고리즘 예
"""
문제1: 동전 문제
- 지불해야 하는 값이 4,720원일 때 1원, 50원, 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.
    - 가장 큰 동전부터 최대한 지불해 값을 채우는 방식으로 구현 가능
    - 탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면 됨
"""
coin_list = [500, 100, 50, 1]

def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse = True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return total_coin_count, details

print("동전 문제: ", min_coin_count(4720, coin_list))

"""
문제2: 부분 배낭 문제 (Fractional Knapsack Problem) -> 쪼갤 수 있어서 Fractional 이라는 표현을 쓴다
- 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
    - 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
    - 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음, 그래서 Fractional Knapsack Problem이라고 부름
    - Fractional Kanpsack Problem의 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함 (0/1 Kanpsack Problem으로 부름)
"""
# 물건 i에 대하여, 앞이 무게(w), 뒤가 가치(v)인 튜플로 리스트를 구성
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

# 무게 대비 가치가 가장 높은 것부터 내림차순 정렬
data_list = sorted(data_list, key=lambda x:x[1] / x[0], reverse = True)
print("데이터리스트: ",data_list) # 데이터리스트:  [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse = True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break # 다음 물건들은 볼 필요가 없으니까 break
    return total_value, details

print("부분 배낭 문제: ", get_max_value(data_list, 30))

