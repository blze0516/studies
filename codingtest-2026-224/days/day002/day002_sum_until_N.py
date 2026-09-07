import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    N = int(input())
    sum = 0
    
    for i in range(1, N + 1):
        if i % 2 == 0:
            sum += i
    print(sum)
    
if __name__ == "__main__":
    solve()
