import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 합과 최댓값을 구하면 한 번만 빼면 된다.
    # 공간복잡도: O(N)  — 원본과 동일. 정수 리스트를 저장한다.
    n = int(input())
    numbers = list(map(int, input().split()))
    total = numbers[0]
    max_num = numbers[0]

    for i in range(1, n):
        total += numbers[i]
        if numbers[i] > max_num:
            max_num = numbers[i]

    print(total - max_num)


if __name__ == "__main__":
    solve()
