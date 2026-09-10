import sys

input = sys.stdin.readline


def get_smaller(a, b):
    if a < b:
        return a
    return b


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 두 수 비교만 한다.
    # 공간복잡도: O(1)  — 정수 변수만 사용한다.
    a, b = map(int, input().split())
    print(get_smaller(a, b))


if __name__ == "__main__":
    solve()
