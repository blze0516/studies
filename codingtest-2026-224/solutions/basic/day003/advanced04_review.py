import sys

input = sys.stdin.readline


def sum_at_least(numbers, k):
    total = 0
    for number in numbers:
        if number >= k:
            total += number
    return total


def solve() -> None:
    # [채점] 로직 정답 / 시간복잡도 오답
    # 시간복잡도: O(N)  — 원본 O(1) 오기재. 정수 N개를 한 번씩 보므로 O(N)
    # 공간복잡도: O(N)  — 정수 리스트를 저장한다.
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(sum_at_least(numbers, k))


if __name__ == "__main__":
    solve()
