import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    print(sum(map(int, input().split())))

if __name__ == "__main__":
    solve()
