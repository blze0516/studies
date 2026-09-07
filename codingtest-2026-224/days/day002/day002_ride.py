import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    age, height = map(int, input().split())
    
    if age >= 14 and height >= 120:
        print("RIDE")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
