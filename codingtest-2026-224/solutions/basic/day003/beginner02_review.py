import sys

input = sys.stdin.readline


def is_even(n):
    return n % 2 == 0


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 나머지 연산과 분기만 한다.
    # 공간복잡도: O(1)  — 정수 변수만 사용한다.
    n = int(input())

    if is_even(n):
        print("EVEN")
    else:
        print("ODD")


if __name__ == "__main__":
    solve()
