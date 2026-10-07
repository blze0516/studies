import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 이웃 쌍 N-1개를 한 번씩 본다.
    # 공간복잡도: O(N)  — 원본과 동일. 정수 리스트를 저장한다.
    n = int(input())
    numbers = list(map(int, input().split()))
    max_sum = numbers[0] + numbers[1]

    for i in range(1, n - 1):
        pair_sum = numbers[i] + numbers[i + 1]
        if pair_sum > max_sum:
            max_sum = pair_sum

    print(max_sum)


if __name__ == "__main__":
    solve()
