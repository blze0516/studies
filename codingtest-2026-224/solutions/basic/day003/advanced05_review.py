import sys

input = sys.stdin.readline


def get_total_price(price, quantity):
    return price * quantity


def get_discounted_price(total_price, discount):
    return total_price - total_price * discount // 100


def can_pay(money, discounted_total_price):
    return money >= discounted_total_price


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 함수가 세 개여도 곱셈·할인·비교만 하므로 고정 횟수다.
    # 공간복잡도: O(1)  — 정수 변수만 사용한다.
    price, quantity, discount, money = map(int, input().split())
    total_price = get_total_price(price, quantity)
    discounted_total_price = get_discounted_price(total_price, discount)

    if can_pay(money, discounted_total_price):
        print(discounted_total_price)
    else:
        print("NO")


if __name__ == "__main__":
    solve()
