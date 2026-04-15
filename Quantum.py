# [양자(Quantum) 알고리즘]
# 양자 역학의 특성(중첩, 얽힘)을 이용한 컴퓨팅 방식
# 특정 문제에서 기존 방식보다 압도적인 속도 향상을 보여줌 (예: 쇼어 알고리즘)

# [시험 꿀팁!]
# 1. 큐비트(Qubit): 0과 1 상태가 동시에 존재할 수 있는 양자 정보의 최소 단위.
# 2. 중첩(Superposition): 여러 상태가 확률적으로 동시에 존재함.
# 3. 측정(Measurement): 관찰하는 순간 하나의 상태로 확정됨 (붕괴).
# 4. 양자 이득(Quantum Speedup): 고전 컴퓨터보다 기하급수적으로 빠른 문제 해결 능력.

import random
import math

def quantum_measurement(state_0, state_1):
    # 알고리즘 진행: 1. 0일 확률과 1일 확률이 공존하는 중첩 상태 준비
    rand_val = random.uniform(0, 1)
    
    # 알고리즘 진행: 2. 확률에 근거하여 결과를 '측정' (관찰)
    if rand_val < state_0:
        return "|0> 로 붕괴(Measured)"
    else:
        return "|1> 로 붕괴(Measured)"

# 알고리즘 진행: 3. 중첩 상태 정의 (예: 50% 확률씩)
p_0 = (1 / math.sqrt(2)) ** 2
p_1 = 1 - p_0

print("--- 양자 중첩 상태 측정 시뮬레이션 ---")
results = {"|0> 로 붕괴(Measured)": 0, "|1> 로 붕괴(Measured)": 0}
for _ in range(100):
    # 알고리즘 진행: 4. 여러 번 반복 측정하여 확률적 분포 확인
    outcome = quantum_measurement(p_0, p_1)
    results[outcome] += 1

print(f"100번 시도 중 결과: {results}")
