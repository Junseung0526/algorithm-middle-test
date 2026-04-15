# [탐색(Search) 알고리즘]
# 방대한 데이터 중에서 원하는 값을 효율적으로 찾는 기법
# 선형 탐색(O(n))부터 이진 탐색(O(log n))까지 다양한 방식이 존재함

# [시험 꿀팁!]
# 1. 이진 탐색은 반드시 '정렬된 데이터'에서만 작동함.
# 2. 매 단계마다 탐색 범위가 절반으로 줄어듦 -> 시간 복잡도 O(log n).
# 3. 데이터가 정렬되어 있지 않다면 선형 탐색(O(n))을 써야 함.

def binary_search(arr, target):
    # 알고리즘 진행: 1. 탐색 범위의 시작(low)과 끝(high) 설정
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        # 알고리즘 진행: 2. 중간점(mid)을 계산하여 찾는 값과 비교
        mid = (low + high) // 2
        
        # 찾았으면 인덱스 반환
        if arr[mid] == target:
            return mid
        # 알고리즘 진행: 3. 찾는 값이 중간값보다 크면 오른쪽 절반 탐색
        elif arr[mid] < target:
            low = mid + 1
        # 알고리즘 진행: 4. 찾는 값이 중간값보다 작으면 왼쪽 절반 탐색
        else:
            high = mid - 1
            
    return -1

data = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(data, target)
print(f"이진 탐색 결과 (값 {target}의 인덱스): {result}")
