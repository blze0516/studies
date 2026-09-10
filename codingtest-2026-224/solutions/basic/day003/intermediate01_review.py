import sys

input = sys.stdin.readline


def get_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 1부터 N까지 N번 더한다.
    # 공간복잡도: O(1)  — 합계 변수만 사용한다.
    n = int(input())
    print(get_sum(n))


if __name__ == "__main__":
    solve()
