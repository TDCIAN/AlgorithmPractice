"""
대표적인 데이터 구조7: 트리

1. 트리(Tree) 구조
- 트리: Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
- 실제로 어디에 많이 사용되나?
    - 트리 중 이진 트리(Binary Tree) 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨

2. 알아둘 용어
- Node: 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
- Root Node: 트리 맨 위에 있는 노드
- Level: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
- Parent Node: 어떤 노드의 다음 레벨에 연결된 노드
- Child Node: 어떤 노드의 상위 레벨에 연결된 노드
- Leaf Node(Terminal Node): Child Node가 하나도 없는 노드
- Sibling (Brother Node): 동일한 Parent Node를 가진 노드
- Depth: 트리에서 Node가 가질 수 있는 최대 Level

3. 이진 트리와 이진 탐색 트리 (Binary Search Tree)
- 이진 트리: 노드의 최대 Branch가 2인 트리
- 이진 탐색 트리(Binary Search Tree, BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
    - 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음

4. 자료 구조 이진 탐색 트리의 장점과 주요 용도
- 주요 용도: 데이터 검색(탐색)
- 장점: 탐색 속도를 개선할 수 있음
"""

# 5. 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기
# 5.1 노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 5.2 이진 탐색 트리에 데이터 넣기
#   - 이진 탐색 트리 조건에 부합하게 데이터를 넣어야 함
class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value: # 루트 노드보다 작다면
                if self.current_node.left != None: # 이미 해당 브랜치를 가지고 있다면
                    self.current_node = self.current_node.left
                else: # 해당 노드 브랜치가 없다면 현재 노드에 새로운 노드를 만들어서 연결시켜준다
                    self.current_node.left = Node(value)
                    break
            else: # 루트 노드보다 크다면
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

head = Node(1) # 루트 노드를 일단 만든다
BST = NodeMgmt(head) # 만들어진 루트 노드를 NodeMgmt에 넣어줌으로써 BinarySearchTree 구조를 가진 객체를 생성
BST.insert(2)

# 이진 탐색 트리를 탐색하기
class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value: # 현재 노드가 내가 찾는 노드라면
                return True
            elif value < self.current_node.value: # 왼쪽이라면
                self.current_node = self.current_node.left # 아예 왼쪽으로 바꿔준다
            else: # 오른쪽이라면
                self.current_node = self.current_node.right # 아예 오른쪽으로 바꿔준다
        return False

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(8)
BST.insert(8)
    
print(BST.search(8)) # True
print(BST.search(6))