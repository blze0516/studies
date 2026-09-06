import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    age, fare = map(int, input().split())
    
    if age <= 7:
        answer = 0
    elif age <= 18:
        answer = fare // 2
    else:
        answer = fare
        
    print(answer)

if __name__ == "__main__":
    solve()
