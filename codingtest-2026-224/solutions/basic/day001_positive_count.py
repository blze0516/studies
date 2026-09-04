import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    numbers = list(map(int, input().split()))
    cnt = 0
    
    for n in numbers:
        if n > 0:
            cnt += 1
            
    print(cnt)

if __name__ == "__main__":
    solve()
