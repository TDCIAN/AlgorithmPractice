"""
대표적인 데이터 구조4: 큐(Queue)
1. 큐 구조
가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
- 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것과 동일
- FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식으로 스택과 꺼내는 순서가 반대

2. 알아둘 용어
- Enqueue: 큐에 데이터를 넣는 기능
- Dequeue: 큐에서 데이터를 꺼내는 기능

3. 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기
- queue 라이브러리에는 다양한 큐 구조로 Queue(), LifoQueue(), PriorityQueue() 제공
- 프로그램을 작성할 때 프로그램에 따라 적합한 자료 구조를 사용
  - Queue(): 가장 일반적인 큐 자료 구조
  - LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조(스택 구조라고 보면 됨)
  - PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력
  -> 일반적인 큐 외에 다양한 정책이 적용된 큐들이 있음
"""

# 3.1 Queue()로 큐 만들기 (가장 일반적인 큐, FIFO(First-In, First-Out))
import queue
data_queue = queue.Queue()
data_queue.put("funcoding") # put이 곧 enqueue임
data_queue.put(1)
print(data_queue.qsize()) # 2
print(data_queue.get()) # funcoding -> get이 곧 dequeue임
print(data_queue.qsize()) # 1
print(data_queue.get())  # 1
print(data_queue.qsize()) # 0

# 3.2 LifoQueue()로 큐 만들기 (LIFO(Last-In, First-Out))
data_queue = queue.LifoQueue()
data_queue.put("FFuncoding")
data_queue.put(333)
print(data_queue.qsize()) # 2
print(data_queue.get()) # 333이 먼저 나옴 -> Last-In First-Out인 LifoQueue니까

# 3.3 PriorityQueue()로 큐 만들기
data_p_queue = queue.PriorityQueue()
data_p_queue.put((10, "Korea")) # PriorityQueue에서는 튜플을 넣게 되는데, 앞에는 우선순위, 뒤에는 자료가 들어감
data_p_queue.put((5, 1)) # 우선순위는 5, 자료는 1이 튜플 형태로 들어감
data_p_queue.put((15, "China"))
print(data_p_queue.qsize()) # 3
print(data_p_queue.get()) # (5, 1)이 출력됨 -> 우선순위가 제일 높으니까
print(data_p_queue.get()) # (10, 'Korea')가 출력됨
"""
참고: 어디에 큐가 많이 쓰일까?
- 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨 (운영체제 참조)
    - 큐의 경우에는 장단점 보다는(특별히 언급되는 장단점이 없음), 큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음
"""

# 4. 프로그래밍 연습
# 연습1: 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0] # 0번 인덱스의 데이터를 삭제
    return data

for index in range(10):
    enqueue(index)

print("결과물: ", queue_list)

for index in range(len(queue_list)):
    dequeue()
    print("디큐 결과물: ",queue_list)
