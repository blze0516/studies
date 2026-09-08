import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 10 7 30
    # 핵심 조건: 현재 경험치 exp, 매일 얻는 경험치 gain, 목표 경험치 target이 주어진다.
    # 매일 gain만큼 경험치가 증가할 때 처음으로 target 이상이 되는 날 수를 출력하라.
    # 처음부터 이미 목표 이상이라면 0을 출력한다.
    # 예상 시간복잡도: O(N)
    exp, gain, target = map(int, input().split())
    days = 0
    
    while exp < target:
        exp += gain
        days += 1
        
    print(days)

    pass


if __name__ == "__main__":
    solve()
