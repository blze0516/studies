import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    money, price = map(int, input().split())
    
    money -= price
    
    print(money)

if __name__ == "__main__":
    solve()
