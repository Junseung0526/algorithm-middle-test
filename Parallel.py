# [병렬(Parallel) 알고리즘]
# 여러 개의 처리 장치(CPU 코어 등)를 사용하여
# 문제를 여러 개의 작은 태스크로 나누어 동시에 실행하는 기법
# 수행 시간을 단축하는 것이 주된 목적

# [시험 꿀팁!]
# 1. 암달의 법칙(Amdahl's Law): 병렬화가 불가능한 순차적인 부분이 전체 성능 향상의 한계를 결정함.
# 2. 오버헤드(Overhead): 프로세스 생성 및 데이터 통신에 드는 비용이 병렬화 이득보다 크면 오히려 느려질 수 있음.
# 3. 데이터 병렬성 vs 작업 병렬성: 데이터를 나누느냐, 서로 다른 작업을 수행하느냐의 차이.

import multiprocessing
import time

def square(number):
    # 알고리즘 진행: 1. 각 워커(코어)가 독립적으로 할당된 숫자의 제곱을 계산
    time.sleep(1) # 부하 가정
    return number * number

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    
    # 순차적 실행 (Sequential)
    start = time.time()
    res_seq = [square(n) for n in numbers]
    print(f"순차 실행 시간: {time.time() - start:.2f}s")
    
    # 병렬 실행 (Parallel)
    start = time.time()
    # 알고리즘 진행: 2. Pool을 통해 사용 가능한 CPU 코어에 작업을 분산 배정
    with multiprocessing.Pool() as pool:
        # 알고리즘 진행: 3. map 함수가 리스트의 원소들을 병렬로 처리함
        res_par = pool.map(square, numbers)
    print(f"병렬 실행 시간: {time.time() - start:.2f}s")
    print(f"병렬 계산 결과: {res_par}")
