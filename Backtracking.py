# [백트랙킹(Backtracking) 알고리즘]
# 해를 찾는 도중, 현재의 경로가 정답이 될 가능성이 없다고 판단되면
# 더 이상 진행하지 않고 되돌아가서 다른 경로를 탐색하는 기법
# "가지치기(Pruning)"를 통해 불필요한 탐색 범위를 줄이는 것이 핵심

# [시험 꿀팁!]
# 1. 상태 공간 트리(State Space Tree): 모든 가능한 경로를 트리로 표현.
# 2. 깊이 우선 탐색(DFS) 기반: 주로 재귀로 구현됨.
# 3. 유망성(Promising) 판단: 현재 노드가 정답 가능성이 있는지 검사하여 탐색 여부를 결정.

def is_safe(board, row, col, n):
    # 알고리즘 진행: 1. 현재 위치에 퀸을 놓을 수 있는지 '유망성' 검사
    for i in range(row):
        # 같은 열, 대각선에 다른 퀸이 있는지 체크
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def n_queens(n, row, board):
    # 알고리즘 진행: 2. 모든 행에 퀸을 놓았다면(성공) 카운트 1 반환
    if row == n:
        return 1
    
    count = 0
    # 알고리즘 진행: 3. 현재 행의 각 열을 하나씩 탐색
    for col in range(n):
        if is_safe(board, row, col, n):
            # 알고리즘 진행: 4. 유망하면 퀸을 배치하고 다음 행으로 진행
            board[row] = col
            count += n_queens(n, row + 1, board)
            # 알고리즘 진행: 5. 되돌아올 때 상태를 복구할 필요는 없으나 논리적으로는 Backtracking 발생
    return count

n = 4
board = [0] * n
print(f"{n}-Queens 해의 개수: {n_queens(n, 0, board)}")
