import sys

input = sys.stdin.readline

def is_free_shipping(price):
    return price >= 30000

def solve() -> None:
    # 입력: 10
    # 핵심 조건: 주문 금액 price가 30000 이상이면 무료 배송이다.
    # is_free_shipping(price) 함수를 작성해 무료 배송 가능 여부를 bool로 반환하고, 메인 코드에서 FREE 또는 PAID를 출력하라.
    # 예상 시간복잡도: O(1)
    price = int(input())
    
    if is_free_shipping(price):
        print("FREE")
    else:
        print("PAID")
    pass


if __name__ == "__main__":
    solve()
