# [분산(Distributed) 알고리즘]
# 여러 대의 독립적인 컴퓨터(노드)들이 네트워크를 통해
# 메시지를 주고받으며 하나의 작업을 함께 수행하는 방식

# [시험 꿀팁!]
# 1. 고장 허용(Fault Tolerance): 일부 노드가 고장 나도 시스템 전체가 작동해야 함.
# 2. 동기화 문제: 여러 노드가 동일한 자원에 접근할 때의 합의(Consensus)가 중요함.
# 3. 확장성(Scalability): 노드 수가 늘어남에 따라 처리 성능이 얼마나 선형적으로 증가하는가.

import queue
import threading
import time

# 알고리즘 진행: 1. 마스터(Master)가 전체 작업을 생성하고 큐(네트워크 채널 역할)에 넣음
def master(task_queue, result_queue, num_tasks):
    for i in range(num_tasks):
        task_queue.put(f"Task_{i}")
    
    # 종료 신호 전송
    for _ in range(3):
        task_queue.put(None)

# 알고리즘 진행: 2. 워커(Worker) 노드들이 네트워크(큐)에서 작업을 가져와 처리
def worker(worker_id, task_queue, result_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break
        
        print(f"Worker {worker_id} 가 {task}를 처리 중...")
        time.sleep(1) # 실제 작업 수행 시뮬레이션
        # 알고리즘 진행: 3. 처리된 결과를 다시 결과 채널로 전달
        result_queue.put(f"{task} 완료 by Worker {worker_id}")

if __name__ == "__main__":
    task_q = queue.Queue()
    result_q = queue.Queue()
    
    workers = []
    for i in range(3):
        w = threading.Thread(target=worker, args=(i, task_q, result_q))
        w.start()
        workers.append(w)
        
    master(task_q, result_q, 6)
    
    for w in workers:
        w.join()
        
    print("모든 분산 처리 결과:")
    while not result_q.empty():
        print(result_q.get())
