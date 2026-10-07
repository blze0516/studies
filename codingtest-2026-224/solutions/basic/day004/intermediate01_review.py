import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. N개를 한 번씩 본다.
    # 공간복잡도: O(N)  — 원본과 동일. 정수 리스트를 저장한다.
    n = int(input())
    numbers = list(map(int, input().split()))
    min_number = numbers[0]

    for i in range(1, n):
        if numbers[i] < min_number:
            min_number = numbers[i]

    print(min_number)


if __name__ == "__main__":
    solve()
