import sys

input = sys.stdin.readline


def count_multiples(n, k):
    count = 0
    for i in range(1, n + 1):
        if i % k == 0:
            count += 1
    return count


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 1부터 N까지 한 번씩 본다.
    # 공간복잡도: O(1)  — 카운터 변수만 사용한다.
    n, k = map(int, input().split())
    print(count_multiples(n, k))


if __name__ == "__main__":
    solve()
