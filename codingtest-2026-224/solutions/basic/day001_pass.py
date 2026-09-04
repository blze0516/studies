import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    score = int(input())

    if(score >= 60):
        print("PASS")
    else:
        print("FAIL")

if __name__ == "__main__":
    solve()
