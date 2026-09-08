import sys

input = sys.stdin.readline

def get_larger(a, b):
    if a > b:
        return a
    return b

def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    a, b = map(int, input().split())
    
    print(get_larger(a, b))
        
    
if __name__ == "__main__":
    solve()
