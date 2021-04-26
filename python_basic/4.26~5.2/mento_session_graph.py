"""
멘토세션 - 4
- 그래프 기반의 고급 알고리즘

- Dijkstra algorithm: Minimum Distance 계산 알고리즘
- Prim's algorithm: Vertex 기반의 MST(Minimum Spanning Tree) 알고리즘
- Kruskal's algorithm: Edge 기반의 MST 알고리즘


- 이론적으로 잘 정리된 알고리즘 vs 현실적으로 사용 가능한 알고리즘
    - Dijkstra algorithm: Minimum Distance 계산 알고리즘
        - 약간의 수정으로 Shortest Path 알고리즘으로 변형 가능
        - 파생된 '최적의 알고리즘' - A*(에이스타) 알고리즘(Literature -> 기존연구)
            - 공간을 굉장히 많이 활용하기 때문에(메모리 차지 많음) 실제로는 사용할 수 없음
        - 상황에 맞는 다양한 Approximation 알고리즘(Research -> 최신연구)

- MST(Minimum Spanning Tree) 알고리즘
    - 최적의 전자회로 Wiring을 위해 개발됨
        - Redundancy(여분, 군더더기) 없이 모든 부품에 전기 공급
        - 최소 코스트로 네트워크 구성 등
    - Maze Generation Algorithm 등에 활용

- Max Flow - Min Cut 알고리즘
    - Duality를 이용한 문제 해결
        - 최대 유량 알고리즘
        - 최대 컷 알고리즘
    - Image Segmentation에 활용

- PageRank 알고리즘
    - 웹사이트 페이지의 중요도를 측정
    - 1998년 Google 서비스로 발전
"""