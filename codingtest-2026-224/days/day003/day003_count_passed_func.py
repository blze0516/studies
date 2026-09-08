import sys

input = sys.stdin.readline

def count_passed(scores):
    count = 0
    
    for score in scores:
        if score >= 60:
            count += 1
    return count    

def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    n = int(input())
    scores = list(map(int, input().split()))
    
    print(count_passed(scores))
        
    
if __name__ == "__main__":
    solve()
