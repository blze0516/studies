import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    a, b = map(int, input().split())
    
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("SAME")

if __name__ == "__main__":
    solve()
