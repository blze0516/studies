import sys

input = sys.stdin.readline

def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    N = int(input())
    
    sales = list(map(int, input().split()))

    total = 0
    
    max_sale = sales[0]
    min_sale = sales[0]
    
    for sale in sales:
        total += sale
        if sale > max_sale:
            max_sale = sale
        if sale < min_sale:
            min_sale = sale
    
    print(total)    
    print(max_sale) 
    print(min_sale)     
    
if __name__ == "__main__":
    solve()