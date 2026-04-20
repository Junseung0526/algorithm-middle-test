# [중간고사 대비] 탐색 알고리즘 시각화 및 테스트 세트

def visualizer(arr, low, mid, high, target):
    """탐색 범위를 시각적으로 보여주는 함수"""
    display = [".."] * len(arr)
    for i in range(low, high + 1):
        display[i] = str(arr[i])
    
    pointer = ["  "] * len(arr)
    pointer[low] = " L"
    pointer[high] = " H"
    pointer[mid] = " M"
    if low == high: pointer[low] = "LHM"
    
    print(f"Target: {target}")
    print(f"Array: {' '.join(display)}")
    print(f"Ptrs: {' '.join(pointer)}")
    print("-" * 30)

def binary_search(arr, target, verbose=True):
    """이진 탐색: 정렬된 리스트에서 타겟 찾기"""
    low = 0
    high = len(arr) - 1
    step = 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if verbose:
            print(f"[Step {step}]")
            visualizer(arr, low, mid, high, target)
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        step += 1
            
    return -1

# --- 시험 대비 테스트 스위트 ---
def run_tests():
    # 이진 탐색은 반드시 정렬된 데이터여야 함
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    targets = [7, 19, 2] # 존재하는 값, 끝 값, 없는 값
    
    for t in targets:
        print(f"\n=== Target {t} 탐색 시작 ===")
        result = binary_search(data, t, verbose=True)
        if result != -1:
            print(f"결과: 인덱스 {result}에서 찾았습니다.")
        else:
            print("결과: 찾지 못했습니다.")

if __name__ == "__main__":
    print("=== 이진 탐색(Binary Search) 시각화 도구 ===")
    run_tests()
