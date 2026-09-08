import sys

input = sys.stdin.readline

def count_even(N):
    count = 0
    
    for i in range(1, N + 1):
        if i % 2 == 0:
            count += 1
    return count

def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    N = int(input())
    
    print(count_even(N))
        
    
if __name__ == "__main__":
    solve()
