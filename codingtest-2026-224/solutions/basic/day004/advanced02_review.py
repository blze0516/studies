import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 합과 개수를 각각 한 번씩 봐도 O(N)
    # 공간복잡도: O(N)  — 원본과 동일. 정수 리스트를 저장한다.
    n = int(input())
    numbers = list(map(int, input().split()))
    total = 0
    count = 0

    for number in numbers:
        total += number

    average = total / n

    for number in numbers:
        if number >= average:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()
