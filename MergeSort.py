# [분할 정복(Divide and Conquer) 알고리즘]
# 분할(Divide): 해결하기 어려운 문제를 동일한 유형의 더 작은 부분 문제들로 나눕니다.
# 정복(Conquer): 나눈 부분 문제들을 재귀적으로 해결합니다. (문제가 충분히 작아지면 직접 해결)
# 결합(Combine): 부분 문제의 정답들을 합쳐서 원래 문제의 정답을 만든다.

# [시험 꿀팁!]
# 1. 합병 정렬의 시간 복잡도는 언제나 O(n log n)으로 일정함 (최악, 평균, 최선 모두 동일).
# 2. 안정 정렬(Stable Sort): 동일한 값의 상대적 순서가 유지됨.
# 3. 공간 복잡도: 정렬 과정에서 추가적인 메모리 공간(배열)이 필요함.

def merge_sort(arr):
    # 알고리즘 진행: 1. 리스트 크기가 1 이하가 될 때까지 반으로 계속 쪼갬 (Divide)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 알고리즘 진행: 2. 쪼개진 부분들을 정렬하면서 다시 합침 (Conquer & Combine)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    # 알고리즘 진행: 3. 왼쪽과 오른쪽 리스트의 첫 원소부터 비교하며 작은 순서대로 결과에 넣음
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 알고리즘 진행: 4. 남은 원소들을 결과 리스트 뒤에 붙임
    result.extend(left[i:])
    result.extend(right[j:])
    return result

data = [38, 27, 43, 3, 9, 82, 10]
print(f"정렬 결과: {merge_sort(data)}")
