import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 구간 계산을 정해진 횟수만 한다.
    # 공간복잡도: O(1)  — 변수 몇 개만 사용한다.
    usage = int(input())
    total = 0

    if usage > 200:
        total += (usage - 200) * 5
        usage -= usage - 200

    if usage > 100:
        total += (usage - 100) * 3
        usage -= usage - 100

    total += usage * 2

    print(total)


if __name__ == "__main__":
    solve()
