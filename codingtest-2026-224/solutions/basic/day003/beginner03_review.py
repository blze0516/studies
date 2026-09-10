import sys

input = sys.stdin.readline


def triple(n):
    return 3 * n


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 곱셈 한 번만 한다.
    # 공간복잡도: O(1)  — 정수 변수만 사용한다.
    n = int(input())
    print(triple(n))


if __name__ == "__main__":
    solve()
