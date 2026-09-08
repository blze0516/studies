import sys

input = sys.stdin.readline

def get_final_price(price, discount):
    return price - price * discount // 100

def can_buy(money, final_price):
    return money >= final_price

def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    money, price, discount = map(int, input().split())
    
    final_price = get_final_price(price, discount)
    
    if can_buy(money, final_price):
        print("BUY")
    else:
        print("NO")
    
if __name__ == "__main__":
    solve()
