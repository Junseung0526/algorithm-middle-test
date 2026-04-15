# [근사(Approximation) 알고리즘]
# 물건을 쪼갤 수 없을 때(0/1 Knapsack) 발생
# 이때는 그리디가 최적해를 보장하지 못함 (NP-Hard 문제)
# 하지만 아주 복잡한 상황에서 빠르게 답을 내야 할 때,
# 그리디 방식을 차용한 근사 알고리즘을 사용함.

# [시험 꿀팁!]
# 1. 근사 비율(Approximation Ratio): 최적해 대비 근사해의 품질을 나타냄 (보통 2배 이내 등을 목표).
# 2. 다항 시간 내에 실행 가능해야 함: 정확한 답은 못 내도 시간은 빨라야 함.
# 3. 0/1 배낭 문제에서 그리디는 '가성비순'으로만 채우면 최악의 경우 매우 낮은 성능을 보일 수 있음.

def approx_knapsack(capacity, items):
    # 알고리즘 진행: 1. 가성비(가치/무게) 순으로 정렬
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    greedy_res = 0
    temp_cap = capacity
    # 알고리즘 진행: 2. 순서대로 넣을 수 있는 만큼 다 넣음 (그리디 해)
    for weight, value in items:
        if temp_cap >= weight:
            temp_cap -= weight
            greedy_res += value

    # 알고리즘 진행: 3. 배낭에 들어가는 물건 중 가장 가치가 큰 단일 품목 선택
    max_single_val = max([item[1] for item in items if item[0] <= capacity])

    # 알고리즘 진행: 4. '그리디 합'과 '가장 큰 단일 품목' 중 더 큰 것을 선택 (이것이 1/2-근사 알고리즘)
    return max(greedy_res, max_single_val)

items = [(10, 60), (20, 100), (30, 120)]
capacity = 30
print(f"근사 알고리즘 결과: {approx_knapsack(capacity, items)}")
