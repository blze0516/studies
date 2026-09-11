import sys

input = sys.stdin.readline

def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    N = int(input())
    
    numbers = list(map(int, input().split()))
    max_value = numbers[0]
    min_value = numbers[0]
    
    for i in range(1, N):
        if numbers[i] > max_value:
            max_value = numbers[i]
        
        if numbers[i] < min_value:
            min_value = numbers[i]
            
    print(min_value, max_value)    
    
if __name__ == "__main__":
    solve()