import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 19
    # 핵심 조건: 19 이상이면 ADULT
    #           19 미만이면 MINOR
    # 예상 시간복잡도: O(1)
    age = int(input())

    if age >= 19:
        print("ADULT")
    else:
        print("MINOR")

    pass


if __name__ == "__main__":
    solve()
