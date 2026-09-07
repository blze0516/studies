import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 10
    # 핵심 조건: 1 <= N <= 100000
    # 예상 시간복잡도: O(1)
    num = int(input())
    count = 0

    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1
        
    print(count)

    pass


if __name__ == "__main__":
    solve()
