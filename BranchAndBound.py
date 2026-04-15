# [분기 한정(Branch and Bound) 알고리즘]
# 백트랙킹처럼 모든 가능한 해를 탐색하지만, 한정 함수(Bound Function)를 사용하여
# 탐색 중인 부분 해가 최적해보다 나빠질 것이 확실하면 탐색을 중지함
# 주로 최적화 문제(최대/최소값 찾기)를 풀 때 사용됨.

# [시험 꿀팁!]
# 1. 너비 우선 탐색(BFS) 또는 최상 우선 탐색(Best-First Search) 기반: 주로 Priority Queue 사용.
# 2. 한정(Bounding): 유망하지 않은 마디(Node)를 잘라내어 탐색 효율 극대화.
# 3. 백트랙킹과의 차이: 백트랙킹은 주로 DFS, 분기한정은 BFS/Best-First 사용.

from queue import PriorityQueue

class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
    
    def __lt__(self, other):
        # 알고리즘 진행: 1. 우선순위 큐에서 Bound(한계치)가 높은 순서대로 꺼냄 (최상 우선 탐색)
        return self.bound > other.bound

def get_bound(node, n, W, items):
    # 알고리즘 진행: 2. 현재 상태에서 앞으로 얻을 수 있는 최대 기대 가치(Bound)를 계산 (Fractional Knapsack 방식 사용)
    if node.weight >= W:
        return 0
    
    profit_bound = node.value
    j = node.level + 1
    total_weight = node.weight
    
    while j < n and total_weight + items[j][0] <= W:
        total_weight += items[j][0]
        profit_bound += items[j][1]
        j += 1
    
    if j < n:
        profit_bound += (W - total_weight) * items[j][1] / items[j][0]
        
    return profit_bound

def knapsack_bb(W, items):
    # 알고리즘 진행: 3. 가성비 순 정렬 후 초기 마디(Root) 생성
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    n = len(items)
    pq = PriorityQueue()
    
    root = Node(-1, 0, 0, 0)
    root.bound = get_bound(root, n, W, items)
    pq.put(root)
    
    max_profit = 0
    while not pq.empty():
        u = pq.get() # 가망성이 높은 노드부터 탐색
        
        # 알고리즘 진행: 4. 현재 노드의 Bound가 현재까지 찾은 최대 이익(max_profit)보다 클 때만 탐색
        if u.bound > max_profit:
            # 왼쪽 자식: 다음 물건을 포함하는 경우
            v_inc = Node(u.level + 1, u.value + items[u.level + 1][1], u.weight + items[u.level + 1][0], 0)
            if v_inc.weight <= W and v_inc.value > max_profit:
                max_profit = v_inc.value
            
            v_inc.bound = get_bound(v_inc, n, W, items)
            if v_inc.bound > max_profit:
                pq.put(v_inc)
                
            # 오른쪽 자식: 다음 물건을 포함하지 않는 경우
            v_exc = Node(u.level + 1, u.value, u.weight, 0)
            v_exc.bound = get_bound(v_exc, n, W, items)
            if v_exc.bound > max_profit:
                pq.put(v_exc)
                
    return max_profit

W = 10
items = [(2, 40), (5, 30), (10, 50), (5, 10)]
print(f"분기 한정 배낭 문제 최적값: {knapsack_bb(W, items)}")
