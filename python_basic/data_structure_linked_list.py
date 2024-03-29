"""
대표적인 데이터 구조5: 링크드 리스트 (Linked List)

1. 링크드 리스트 (Linked List) 구조
- 연결 리스트라고도 함
- 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
- 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
- 본래 C언어에서는 주요한 데이터 구조이지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원

- 링크드 리스트 기본 구조와 용어
    - 노드(Node): 데이터 저장 단위 (데이터값, 포인터)로 구성
    - 포인터(Pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간
"""
"""
2. 간단한 링크드 리스트 예
Node 구현
- 보통 파이썬에서 링크드 리스트 구현시, 파이썬 클래스를 활용함
    - 파이썬 객체지향 문법 이해 필요
    - 참고: https://www.funcoding.org/PL&OOP1-3.html
"""
class Node:
    def __init__(self, data, next=None): # 데이터와 다음 데이터의 주소
        self.data = data
        self.next = next
# Node와 Node 연결하기 (포인터 활용)
node1 = Node(1)
node2 = Node(2)
node1.next = node2 # 이런 방식으로 node1과 node2를 연결함
head = node1 # 가장 앞 노드의 주소를 알기 위해서 만든 head 변수

# 링크드 리스트로 데이터 추가하기
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data) # node의 next가 None일 때 인자로 받는 데이터(data)로 새로운 객체를 생성하고 연결됨

node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

# 링크드 리스트 데이터 출력하기(검색하기)
node = head
while node.next:
    print(node.data, end=',')
    node = node.next
print("마지막:", node.data) 
# 출력결과: 1,2,3,4,5,6,7,8,마지막: 9

"""
3. 링크드 리스트의 장단점 (전통적인 C언어에서의 배열과 링크드 리스트)
- 장점
    - 데이터 공간을 미리 할당하지 않아도 됨
        - 배열은 미리 데이터 공간을 할당 해야 함

- 단점
    - 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
    - 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
    - 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요
"""
"""
4. 링크드 리스트의 복잡한 기능1 (링크드 리스트 데이터 사이에 데이터를 추가)
- 링크드 리스트는 유지 관리에 부가적인 구현이 필요함
"""
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

# 새 노드를 1과 2 사이에 삽입
node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False # node3(1.5)를 1 다음에 넣고 싶으니까 1에서 반복문을 멈춰야 한다
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

# 5. 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '': # 데이터가 없는 경우를 대비한 방어코드
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data) # 마지막 노드에 새로 생성된 노드를 추가
    
    def desc(self):
        node = self.head
        while node:
            print("Node.desc:", node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':  # 데이터가 없는 경우를 대비한 방어코드
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data: # 경우의 수1: head를 삭제하는 경우 - self.head를 바꿔줘야 함
            temp = self.head # self.head 객체를 삭제하기 위해 임시로 temp에 담아서 객체를 삭제했음
            self.head = self.head.next # 만약 self.head 객체를 삭제하면, 이 코드가 실행이 안되기 때문
            del temp
        else: 
            node = self.head
            while node.next: # 경우의 수2: self.head가 아닌 노드를 삭제해야 할 경우(중간 or 끝)
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next # 삭제된 노드 다음 노드를 이전 노드와 연결시킴
                    del temp # node의 next를 삭제함
                    return
                else:
                    node = node.next # 마지막 노드 삭제
        
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

linkedlist1 = NodeMgmt(0)
# print("desc 결과:",linkedlist1.desc())

for data in range(1, 10):
    linkedlist1.add(data)
print("desc 결과:",linkedlist1.desc())

"""
6. 링크드 리스트의 복잡한 기능2 (특정 노드를 삭제)
    - 다음 코드는 위의 코드에서 delete 메서드만 추가한 것이므로 해당 메서드만 확인하면 됨
"""
# 테스트를 위해 1개 노드를 만들어 봄
linkedlist1 = NodeMgmt(0)
print("line 159: ", linkedlist1.desc()) # None
# head가 살아있음을 확인
print("line 161: ", linkedlist1.head) # <__main__.Node object at 0x7fa0dfa3cdf0>
# head를 지워봄(위에서 언급한 경우의 수 1)
print("line 163: ", linkedlist1.delete(0)) # None
# 다음 코드 실행시 아무것도 안나온다는 것은 linkedlist1.head가 정상적으로 삭제되었음을 의미
print("line 165: ", linkedlist1.head) # None
# 다시 하나의 노드를 만들어봄
linkedlist1 = NodeMgmt(0)
print("line 168: ", linkedlist1.desc()) # None
# 여러 노드를 더 추가하기
for data in range(1, 10):
    linkedlist1.add(data)
print("line 172: ", linkedlist1.desc())

# 노드 중에 하나를 삭제하기 (위에서 언급한 경우의 수 2)
linkedlist1.delete(4)
print("line 176: ", linkedlist1.desc()) # 4가 사라짐
linkedlist1.delete(9)
print("line 178: ", linkedlist1.desc()) # 9가 사라짐

"""
7. 다양한 링크드 리스트 구조
- 더블 링크드 리스트(Doubly linked list) 기본 구조
    - 이중 연결 리스트라고도 함
    - 장점: 양방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능
"""
class Node:
    # 그냥 linked list와 다른 점은 주소가 앞(prev), 뒤(next)로 있다는 점임
    def __init__(self, data, prev=None, next=None): 
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        # linked list에서는 head만 있지만, doubly linked list는 뒤에서부터도 검색할 수 있기 때문에 tail도 있다.
        self.tail = self.head 
    
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next: # 주소가 존재할 때까지 반복 -> 노드의 끝을 찾아감
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data): # head를 검색하는 함수
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        # 전체를 검색해봤는데 해당 노드가 없다면 False 리턴
        return False

    def search_from_tail(self, data): # tail을 검색하는 함수
        if self.head == None:
            return False
        
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data): # 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수
        if self.head == None:
            self.head = Node(data)
            return True
        else: # head가 있다는 것은 double linked list가 있다는 말임
            node = self.tail # 맨 뒤에서부터 노드 검색을 할 거니까
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False # 어디에 넣어야 할 지 모르겠으면 False를 리턴하고 끝낸다
            new = Node(data)
            before_new = node.prev # 원래 노드의 앞에 있는 노드를 가리킨다
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True
        

"""
연습3: 위 코드에서 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수를 만들고, 테스트 해보기
- 더블 링크드 리스트의 tail에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
- 테스트: 임의로 0~9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 2인 노드 앞에 1.5 데이터 값을 가진 노드를 추가해보기
"""
double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
    
print("double_linked_list=",double_linked_list.desc())

print(double_linked_list.search_from_head(3))
node3 = double_linked_list.search_from_head(3)
print("node3.data = ",node3.data)

node3 = double_linked_list.search_from_head(10)
if node3:
    print(node3.data)
else:
    print("No data")

node4 = double_linked_list.search_from_tail(4)
print("node4.data = ", node4.data)

"""
연습3: 위 코드에서 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수를 만들고, 테스트해보기
- 더블 링크드 리스트의 tail에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
- 테스트: 임의로 0~9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 2인 노드 앞에 1.5 데이터 값을 가진 노드를 추가해보기
"""
double_linked_list.insert_before(1.5, 2) # 1.5를 2 앞에 넣는다
print("insert_before = ",double_linked_list.desc())
