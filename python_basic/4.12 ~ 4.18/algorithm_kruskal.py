
# 6. 크루스칼 알고리즘 (Kruskal's algorithm) 코드 작성
mygraph = { # 'vertices(벌디시스)는 정점(꼭지점, Vertex)의 복수형
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges':[
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

edges = mygraph['edges']
edges.sort()
# print("소트된 엣지스: ",edges)

parent = dict()
rank = dict()

# 노드를 가져오는 find 함수
def find(node):
    # path compression 기법 사용 -> 맨 위의 루트 노드를 현재 노드의 부모(루트 노드)로 만들어 준다
    if parent[node] != node: # 자기 노드의 부모 노드가 자기가 아니라는 것은 루트노드가 아니라는 것을 의미
        parent[node] = find(parent[node])
    return parent[node] # 루트 노드 리턴

# 두 부분 집합의 루트 노드의 랭크를 확인해 낮은 쪽에 붙인다. 같은 경우에는 한쪽을 높인 다음 붙인다(union-by-rank 기법).
def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]: # root1의 랭크가 root2의 랭크보다 높다면 rank1을 rank2의 부모 노드로 붙인다
        parent[root2] = root1
    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list() # 간선 정보에 대한 리스트
    
    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)
    
    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결(사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge # 거리와 두 노드가 들어간다
        if find(node_v) != find(node_u): # 두 노드의 루트 노드가 같은지 다른지 확인 -> 같으면 버려야 한다(사이클 생기니까)
            union(node_v, node_u)
            mst.append(edge)

    return mst

print("크루스칼: ", kruskal(mygraph))
# 크루스칼:  [(5, 'A', 'D'), (5, 'C', 'E'), (6, 'D', 'F'), (7, 'A', 'B'), (7, 'B', 'E'), (9, 'E', 'G')]
"""
7. 시간 복잡도
- 크루스칼 알고리즘의 시간 복잡도는 O(ElogE)
    - 다음 단계에서 2번, 간선을 비용 기준으로 정렬하는 시간에 좌우됨(즉 간선을 비용 기준으로 정렬하는 시간이 가장 큼)
    - 모든 정점을 독립적인 집합으로 만든다.
    - 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
        - 퀵소트를 사용한다면 시간 복잡도는 O(nlogn)이며, 간선이 n이므로 O(ElogE)
    - 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.
      (최소 신장 트리는 사이클이 없으므로, 사이클이 생기지 않도록 하는 것임)
        - union-by-rank와 path compression 기법 사용시 시간 복잡도가 결국 상수값에 가까움, O(1)
"""