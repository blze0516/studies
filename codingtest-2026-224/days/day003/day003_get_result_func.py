import sys

input = sys.stdin.readline

def get_result(score):
    if score >= 60:
        return "PASS"
    return "FAIL"

def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    score = int(input())
    
    print(get_result(score))
        
    
if __name__ == "__main__":
    solve()
