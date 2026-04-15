# 분산(Distributed) 알고리즘
# 여러 대의 독립적인 컴퓨터(노드)들이 네트워크를 통해
# 메시지를 주고받으며 하나의 작업을 함께 수행하는 방식
# 확장성(Scalability)과 고가용성(Availability)이 핵심

import queue
import threading
import time

# 간단한 마스터-워커 분산 모델 시뮬레이션
def master(task_queue, result_queue, num_tasks):
    for i in range(num_tasks):
        task_queue.put(f"Task_{i}")
    
    # 워커들 종료 신호
    for _ in range(3):
        task_queue.put(None)

def worker(worker_id, task_queue, result_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break
        
        # 실제 분산 환경에서는 다른 장치에서 계산되나 여기서는 스레드로 시뮬레이션
        print(f"Worker {worker_id} 가 {task}를 처리 중...")
        time.sleep(1) # 부하 가정
        result_queue.put(f"{task} 완료 by Worker {worker_id}")

if __name__ == "__main__":
    task_q = queue.Queue()
    result_q = queue.Queue()
    
    # 워커 생성
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
