"""
대표적인 데이터 구조8: 힙
1. 힙(Heap)이란?
- 힙: 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
    - 완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

- 힙을 사용하는 이유
    - 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n)이 걸림
    - 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면, O(logn)이 걸림
    - 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

2. 힙(Heap) 구조
- 힙은 최대값을 구하기 위한 구조(최대 힙, Max Heap)와, 최소값을 구하기 위한 구조(최소 힙, Min Heap)로 분류할 수 있음
- 힙은 다음과 같이 두 가지 조건을 가지고 있는 자료구조임
    1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다(최대 힙의 경우).
        - 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음
    2. 완전 이진 트리 형태를 가짐

힙과 이진 탐색 트리의 공통점과 차이점
- 공통점: 힙과 이진 탐색 트리는 모두 이진 트리임
- 차이점:
    - 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
    - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
    - 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
        - 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
- 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면 됨

3. 힙(Heap) 동작
- 데이터를 힙 구조에 삽입, 삭제하는 과정을 그림을 통해 선명하게 이해하기
- https://www.fun-coding.org/Chapter11-heap.html

힙에 데이터 삽입하기 - 기본 동작
- 힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입

힙에 데이터 삽입하기 - 삽입할 데이터가 힙의 데이터보다 클 경우 (Max Heap의 예)
- 먼저 삽입된 데이터는 완전 이진 트리 구조에 맞추어, 최하단부 왼쪽 노드부터 채워짐
- 채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복함(swap)

힙에 데이터 삭제하기 (Max Heap의 예)
- 보통 삭제는 최상단 노드(root 노드)를 삭제하는 것이 일반적임
    - 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임
- 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드(일반적으로 가장 마지막에 추가한 노드)를 root 노드로 이동
- root 노드의 값이 child node보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와
  root 노드 위치를 바꿔주는 작업을 반복함(swap)

4. 힙 구현
힙과 배열
- 일반적으로 힙 구현시 배열 자료구조를 활용함
- 배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면, 구현이 좀 더 수월함
    - 부모 노드 인덱스 번호(parent node's index) = 자식 노드 인덱스 번호(child node's index) // 2
    - 왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호(parent node's index) * 2
    - 오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호(parent node's index) * 2 + 1

힙 클래스 구현3 - insert2
    - 삽입한 노드가 부모 노드의 값보다 클 경우, 부모 노드와 삽입한 노드 위치를 바꿈
    - 삽입한 노드가 루트 노드가 되거나, 부모 노드보다 값이 작거나 같을 경우까지 반복

특정 노드의 관련 노드 위치 알아내기
    - 부모 노드 인덱스 번호(parent node's index) = 자식 노드 인덱스 번호(child node's index) // 2
    - 왼쪽 자식 노드 인덱스 번호(left child node's index) = 부모 노드 인덱스 번호(parent node's index) * 2
    - 오른쪽 자식 노드 인덱스 번호(right child node's index) = 부모 노드 인덱스 번호(parent node's index) * 2 + 1

힙에 데이터 삭제 구현(Max Heap 예)
- 힙 클래스 구현4 - delete1
- 보통 삭제는 최상단 노드(root 노드)를 삭제하는 것이 일반적임
    - 힙의 용도는 최대값 또는 최소값을 root 노드에 넣어서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임

- 힙 클래스 구현4 - delete2
    - 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드(일반적으로 가장 마지막에 추가한 노드)를 root 노드로 이동
    - root 노드의 값이 child node보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와
      root 노드 위치를 바꿔주는 작업을 반복함 (swap)

- 특정 노드의 관련 노드 위치 알아내기
    - 부모 노드 인덱스 번호(parent node's index) = 자식 노드 인덱스 번호(child node's index) // 2
    - 왼쪽 자식 노드 인덱스 번호(left child node's index) = 부모 노드 인덱스 번호(parent node's index) * 2
    - 오른쪽 자식 노드 인덱스 번호(right child node's index) = 부모 노드 인덱스 번호(parent node's index) * 2 + 1

5. 힙(Heap) 시간 복잡도
- depth(트리의 높이)를 h라고 표기한다면,
- n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로
  h = log2n에 가까우므로, 시간 복잡도는 O(logn)
    - 참고: 빅오 표기법에서 logn에서의 log의 밑은 10이 아니라, 2입니다.
    - 한 번 실행시마다, 50%의 실행할 수도 있는 명령을 제거한다는 의미. 즉 50%의 실행시간을 단축시킬 수 있다는 것을 의미함
"""

# 힙에 데이터 삽입 구현 (Max Heap 예)
# 힙 클래스 구현 1
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    # 상위 노드와 관계에서 이 노드가 더 커서 상위 노드와 바꿔야 하는지, 
    # 또는 이 노드가 아예 루트에 있어서 루트 노드와 바꿀 필요가 없는 것인지 판단하는 move_up 메소드
    def move_up(self, inserted_idx):
        if inserted_idx <= 1: # inserted_idx가 루트 노드와 같다면
            return False # 따로 뭘 할 필요가 없으니까 False를 리턴한다
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    # 데이터 추가
    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        # 루트 노드가 아닐 때
        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        # True 면 바꿔줘야 함
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            # inserted_idx와 parent_idx를 swap 해준다
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        if left_child_popped_idx >= len(self.heap_array):
            return False
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return False
            else:
                return False
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    # 삭제하는 메소드
    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        # 맨 끝에 있는 데이터를 root 위치(1번)로 바꿔준다
        self.heap_array[1] = self.heap_array[-1]
        # 바꿔주고 나면 마지막 인덱스는 지워준다
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1   

            if right_child_popped_idx >= len(self.heap_array):
                # swap
                self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                popped_idx = left_child_popped_idx
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
                else:
                    self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = right_child_popped_idx

        return returned_data

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
# 20이 제일 마지막에 들어갔음에도 불구하고 첫 번째 인덱스에 있다
print("힙어레이: ",heap.heap_array) # [None, 20, 10, 15, 5, 4, 8]
print(heap.pop()) # pop을 하면 항상 root의 값이 먼저 나온다 -> 20이 나옴
print("20 빠진 힙어레이: ", heap.heap_array) # [None, 15, 10, 8, 5, 4]
print(heap.pop()) # 15
print("15 빠진 힙어레이: ", heap.heap_array) # [None, 10, 4, 8, 5]



