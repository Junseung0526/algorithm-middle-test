# Algorithm Study Repository

## 1. 개요
이 레포지토리는 알고리즘 중간고사 대비를 위해 핵심 개념 이론과 파이썬 구현 코드를 체계적으로 정리한 공간입니다. 각 알고리즘의 동작 원리뿐만 아니라 시험에서 중요하게 다뤄지는 성능 분석(시간/공간 복잡도)과 최적화 전략을 포함하고 있습니다.

## 2. 프로젝트 구조 (Directory Structure)

## 2. 프로젝트 구조 (Directory Structure) - [중간고사 특화 리뉴얼 완료!]

### 2.1. Concepts (개념 정리) 📝
시험 직전 5분 요약을 위해 **Why?, 1줄 암기 포인트, 시험 빈출 Q&A, 비교표** 형식으로 개편되었습니다.

- [01_Sort_정렬.md](./Concepts_개념정리/01_Sort_정렬.md)
- [02_Search_탐색.md](./Concepts_개념정리/02_Search_탐색.md)
- [03_1_Greedy_Basic.md](./Concepts_개념정리/03_1_Greedy_Basic.md)
- [03_2_Greedy_Graph.md](./Concepts_개념정리/03_2_Greedy_Graph.md)
- [03_3_Greedy_App.md](./Concepts_개념정리/03_3_Greedy_App.md)
- [04_Backtracking_백트래킹.md](./Concepts_개념정리/04_Backtracking_백트래킹.md)

### 2.2. Codes (소스 코드) 💻
단순한 코드 구현을 넘어, 실행 시 **단계별 시각화(Visualizer)**와 **시험 대비 테스트 케이스**를 포함합니다.

- `python Codes_소스코드/01_Sort_정렬.py`: 퀵/합병/삽입 정렬의 데이터 이동 시각화
- `python Codes_소스코드/02_Search_탐색.py`: 이진 탐색의 L, M, H 포인터 이동 시각화
- `python Codes_소스코드/03_1_Greedy_Basic.py`: 배낭 문제 가성비 계산 및 거스름돈 사례 시각화
- `python Codes_소스코드/03_2_Greedy_Graph.py`: 크루스칼 간선 선택 및 다익스트라 거리 갱신 시각화
- `python Codes_소스코드/03_3_Greedy_App.py`: 허프만 트리 생성 및 집합 커버 과정 시각화

## 3. 학습 가이드 (중간고사 필승법)
1. **이론 요약**: `Concepts` 문서의 **[1줄 암기 포인트]**를 읽으며 외웁니다.
2. **시각적 이해**: `Codes` 파일을 실행하여 터미널에 출력되는 **[Step-by-Step]** 과정을 눈으로 따라갑니다.
3. **취약점 점검**: **[시험 빈출 Q&A]**의 질문에 스스로 답할 수 있는지 체크합니다.

## 4. 환경 설정 
```bash
pip install -r requirements.txt
```
