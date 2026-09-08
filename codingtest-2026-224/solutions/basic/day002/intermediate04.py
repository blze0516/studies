import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 4
    #       0
    #       5
    #       10
    #       35
    # 핵심 조건: 첫 줄에 날짜 수 N이 주어진다. 다음 N줄에 하루의 지각 시간 late가 분 단위로 주어진다.
    # 벌점 규칙:
    # 30분 이상: 3점
    # 10분 이상 30분 미만: 2점
    # 1분 이상 10분 미만: 1점
    # 0분: 0점
    # N일의 총 벌점을 출력하라.
    # 예상 시간복잡도: O(N)
    N = int(input())
    total = 0
    
    for _ in range(N):
        late = int(input())
        if late >=  30:
            total += 3
        elif late >= 10:
            total += 2
        elif late >= 1:
            total += 1
        
    print(total)

    pass


if __name__ == "__main__":
    solve()
