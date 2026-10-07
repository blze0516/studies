import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 이웃 쌍 N-1개를 한 번씩 본다.
    # 공간복잡도: O(N)  — 원본과 동일. 정수 리스트를 저장한다.
    n = int(input())
    numbers = list(map(int, input().split()))
    max_increase = 0

    for i in range(1, n):
        if numbers[i] > numbers[i - 1]:
            increase = numbers[i] - numbers[i - 1]
            if increase > max_increase:
                max_increase = increase

    print(max_increase)


if __name__ == "__main__":
    solve()
