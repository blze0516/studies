import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 한 번의 순회로 최댓값과 최솟값을 구한다.
    # 공간복잡도: O(N)  — 원본과 동일. 정수 리스트를 저장한다.
    n = int(input())
    numbers = list(map(int, input().split()))
    max_num = numbers[0]
    min_num = numbers[0]

    for i in range(1, n):
        if numbers[i] > max_num:
            max_num = numbers[i]
        if numbers[i] < min_num:
            min_num = numbers[i]

    print(max_num - min_num)


if __name__ == "__main__":
    solve()
