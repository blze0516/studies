import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 5
    # 핵심 조건: 1 <= N <= 10000
    # 예상 시간복잡도: O(N)
    num = int(input())
    sum = 0

    for i in range(1, num + 1):
        sum += i
        
    print(sum)

    pass


if __name__ == "__main__":
    solve()
