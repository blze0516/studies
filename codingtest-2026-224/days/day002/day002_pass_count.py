import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    n = int(input())
    count = 0
    
    for _ in range(n):
        score = int(input())
        if score >= 60:
            count += 1
            
    print(count)
        
    
if __name__ == "__main__":
    solve()
