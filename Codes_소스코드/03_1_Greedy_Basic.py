# [중간고사 대비] 탐욕 알고리즘 기초 시각화 및 테스트 세트

def fractional_knapsack_visualizer(capacity, items):
    """배낭 문제 과정을 시각화하여 보여주는 함수"""
    # 1. 가성비(Value/Weight) 계산 및 정렬
    # item: (value, weight, name)
    sorted_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0
    current_capacity = capacity
    print(f"배낭 총 용량: {capacity}")
    print("-" * 40)
    
    for v, w, name in sorted_items:
        efficiency = v / w
        if current_capacity <= 0: break
        
        print(f"물건 {name}: 가치={v}, 무게={w}, 가성비={efficiency:.2f}")
        
        if current_capacity >= w:
            # 통째로 넣음
            total_value += v
            current_capacity -= w
            print(f"  => [통째로 넣기] 남은 용량: {current_capacity}, 현재 가치 합: {total_value}")
        else:
            # 쪼개서 넣음
            fraction = current_capacity / w
            added_value = v * fraction
            total_value += added_value
            print(f"  => [쪼개 넣기] {fraction*100:.1f}% 만큼 담음. 현재 가치 합: {total_value}")
            current_capacity = 0
            
    print("-" * 40)
    return total_value

def coin_change_visualizer(money, coins):
    """거스름돈 문제 시각화"""
    coins.sort(reverse=True)
    print(f"목표 금액: {money}원 | 동전 종류: {coins}")
    
    result = {}
    remaining = money
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining %= coin
            print(f"{coin}원 동전: {count}개 사용 (남은 금액: {remaining}원)")
            
    return result

# --- 시험 대비 테스트 스위트 ---
def run_tests():
    # 1. 배낭 문제
    print("\n=== [Test 1] Fractional Knapsack (분할 가능 배낭) ===")
    items = [(60, 10, 'A'), (100, 20, 'B'), (120, 30, 'C')]
    capacity = 50
    final_val = fractional_knapsack_visualizer(capacity, items)
    print(f"최종 가치: {final_val}")

    # 2. 거스름돈 문제 (그리디가 되는 경우)
    print("\n=== [Test 2] Coin Change (그리디 최적해 보장) ===")
    target_money = 1260
    coin_types = [500, 100, 50, 10]
    coin_change_visualizer(target_money, coin_types)

    # 3. 거스름돈 문제 (그리디가 안 되는 경우 - 시험 단골!)
    print("\n=== [Test 3] Coin Change (그리디 최적해 실패 사례) ===")
    target_money = 800
    coin_types_fail = [500, 400, 100]
    print("설명: 그리디는 500+100+100+100(4개)을 선택하지만, 실제 최적해는 400+400(2개)입니다.")
    coin_change_visualizer(target_money, coin_types_fail)

if __name__ == "__main__":
    print("=== 탐욕 알고리즘(Greedy) 기초 시각화 도구 ===")
    run_tests()
