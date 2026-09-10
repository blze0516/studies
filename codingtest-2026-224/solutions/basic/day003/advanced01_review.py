import sys

input = sys.stdin.readline


def get_final_price(price, discount):
    return price - price * discount // 100


def can_buy(money, final_price):
    return money >= final_price


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 할인 계산과 비교만 한다. 함수가 두 개여도 고정 횟수다.
    # 공간복잡도: O(1)  — 정수 변수만 사용한다.
    money, price, discount = map(int, input().split())
    final_price = get_final_price(price, discount)

    if can_buy(money, final_price):
        print("BUY")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
