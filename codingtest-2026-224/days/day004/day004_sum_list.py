import sys

input = sys.stdin.readline

def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    N = int(input())
    
    numbers = list(map(int, input().split()))

    total = 0
    
    for number in numbers:
        total += number
    
    print(total)        
    
if __name__ == "__main__":
    solve()