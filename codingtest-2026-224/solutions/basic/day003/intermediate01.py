import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 42000
    # 핵심 조건: 0 <= price <= 1000000
    # 예상 시간복잡도: O(1)
    price = int(input())

    if price >= 50000:
        delivery_fee = 0
    elif price >= 30000:
        delivery_fee = 2500
    else:
        delivery_fee = 4000
        
    print(delivery_fee)

    pass


if __name__ == "__main__":
    solve()
