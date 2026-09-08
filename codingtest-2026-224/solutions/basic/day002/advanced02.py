from itertools import count
import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 250
    # 핵심 조건: 첫 줄에 N이 주어진다. 다음 N줄에는 각 날의 출석 여부가 1 또는 0으로 주어진다.
    # 점수 규칙:
    # 결석 0: 그날 0점, 연속 출석 수를 0으로 초기화
    # 출석 1: 연속 출석 수를 1 증가시키고, 그 연속 출석 수만큼 점수 획득
    # 총점을 출력하라.
    # 예를 들어 출석 기록이 1, 1, 0, 1이라면 획득 점수는 1 + 2 + 0 + 1 = 4다.
    # 예상 시간복잡도: O(1)
    N = int(input())
    score = 0
    continous = 0
    
    for _ in range(N):
        attend = int(input())
        
        if attend == 0:
            continous = 0
        else:
            continous += 1
            score += continous
            
    print(score)    
    pass


if __name__ == "__main__":
    solve()
