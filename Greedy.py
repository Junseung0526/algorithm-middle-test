# [탐욕(Greedy) 알고리즘]
# 매 순간마다 그 당시 가장 좋다고 생각되는 것을 선택
# 이 방식이 전체적으로 최적의 해답이 되길 바라는 것
# 하지만 모든 문제에서 통하는 것은 아니기에
# 지금의 최선이 나중에도 최선인가? 를 판단하는게 핵심

# [시험 꿀팁!]
# 1. 탐욕적 선택 속성(Greedy Choice Property): 앞의 선택이 이후의 선택에 영향을 주지 않아야 함.
# 2. 최적 부분 구조(Optimal Substructure): 문제의 최적해가 부분 문제의 최적해들로 구성되어야 함.
# 3. 배낭 문제 종류(Fractional vs 0/1): Fractional은 그리디 가능, 0/1은 동적계획법이나 분기한정이 필요함.

def greedy(capacity, items):
    # 알고리즘 진행: 1. 단위 무게당 가치가 가장 높은 순으로 정렬 (가성비 정렬)
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    for weight, value in items:
        # 알고리즘 진행: 2. 배낭에 통째로 넣을 수 있으면 넣음
        if capacity >= weight:
            capacity -= weight
            total_value += value
        # 알고리즘 진행: 3. 남은 무게가 작으면 쪼개서 넣음 (Fractional Knapsack의 핵심)
        else:
            fraction = capacity / weight
            total_value += fraction * value
            break

    return total_value

items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
print(f"그리디 배낭 결과: {greedy(capacity, items)}")
