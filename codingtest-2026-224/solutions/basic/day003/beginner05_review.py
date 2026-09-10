import sys

input = sys.stdin.readline


def is_free_shipping(price):
    return price >= 30000


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 경계값 비교만 한다.
    # 공간복잡도: O(1)  — 정수 변수만 사용한다.
    price = int(input())

    if is_free_shipping(price):
        print("FREE")
    else:
        print("PAID")


if __name__ == "__main__":
    solve()
