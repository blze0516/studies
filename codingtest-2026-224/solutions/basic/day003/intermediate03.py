import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 5
    #       3
    #       0
    #       -2
    #       7
    #       1
    # 핵심 조건: 첫 줄에 N이 주어진다. 다음 N줄에 정수가 하나씩 주어진다. 0보다 큰 수의 개수를 출력하라.
    # 예상 시간복잡도: O(1)
    N = int(input())
    count = 0
    
    for _ in range(N):
        n = int(input())
        if n > 0:
            count += 1
    print(count)

    pass


if __name__ == "__main__":
    solve()
