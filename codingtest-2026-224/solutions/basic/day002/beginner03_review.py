import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 1부터 N까지 N번 출력한다.
    # 공간복잡도: O(1)  — 반복 변수만 사용한다.
    num = int(input())

    for i in range(1, num + 1):
        print(i)


if __name__ == "__main__":
    solve()
