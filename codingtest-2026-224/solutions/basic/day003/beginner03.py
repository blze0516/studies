import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 4
    # 핵심 조건: 양의 정수 N이 주어진다. 1부터 N까지 한 줄에 하나씩 출력하라.
    # 예상 시간복잡도: O(N)
    num = int(input())

    for i in range(1, num + 1):
        print(i)

    pass


if __name__ == "__main__":
    solve()
