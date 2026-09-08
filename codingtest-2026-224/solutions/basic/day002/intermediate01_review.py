import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 구간 비교만 한다.
    # 공간복잡도: O(1)  — 변수 몇 개만 사용한다.
    price = int(input())

    if price >= 50000:
        delivery_fee = 0
    elif price >= 30000:
        delivery_fee = 2500
    else:
        delivery_fee = 4000

    print(delivery_fee)


if __name__ == "__main__":
    solve()
