import sys

input = sys.stdin.readline


def get_positive_info(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
            count += 1
    return total, count


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 정수 N개를 한 번씩 본다.
    # 공간복잡도: O(N)  — 정수 리스트를 저장한다.
    n = int(input())
    numbers = list(map(int, input().split()))
    total, count = get_positive_info(numbers)
    print(total, count)


if __name__ == "__main__":
    solve()
