import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 7
    # 핵심 조건: 짝수면 EVEN, 홀수면 ODD를 출력하라.
    # 예상 시간복잡도: O(1)
    num = int(input())

    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

    pass


if __name__ == "__main__":
    solve()
