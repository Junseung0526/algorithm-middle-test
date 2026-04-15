# [정렬(Sort) 알고리즘]
# 데이터를 특정한 기준(오름차순, 내림차순 등)에 따라 나열하는 기법
# 효율적인 정렬은 탐색 등 다른 알고리즘의 성능에 큰 영향을 미침

# [시험 꿀팁!]
# 1. 퀵 정렬의 평균 복잡도는 O(n log n)이지만, 최악의 경우 O(n^2)가 될 수 있음 (이미 정렬된 경우 등).
# 2. 피벗(Pivot) 선택 방식에 따라 성능이 좌우됨.
# 3. 제자리 정렬(In-place Sort): 추가적인 메모리 공간을 거의 사용하지 않음 (이 코드는 이해를 위해 리스트를 생성함).

def quick_sort(arr):
    # 알고리즘 진행: 1. 리스트가 비었거나 하나면 정렬 완료
    if len(arr) <= 1:
        return arr
    
    # 알고리즘 진행: 2. 기준점(Pivot)을 하나 정함 (여기서는 가운데 원소)
    pivot = arr[len(arr) // 2]
    
    # 알고리즘 진행: 3. 피벗을 기준으로 작은 값, 같은 값, 큰 값으로 리스트를 나눔 (Partition)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 알고리즘 진행: 4. 작은 쪽과 큰 쪽을 재귀적으로 다시 정렬하고 합침
    return quick_sort(left) + middle + quick_sort(right)

data = [3, 6, 8, 10, 1, 2, 1]
print(f"퀵 정렬 결과: {quick_sort(data)}")
