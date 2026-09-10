import sys

input = sys.stdin.readline


def count_passed(scores):
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    return count


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 점수 N개를 한 번씩 본다.
    # 공간복잡도: O(N)  — 점수 리스트를 저장한다.
    n = int(input())
    scores = list(map(int, input().split()))
    print(count_passed(scores))


if __name__ == "__main__":
    solve()
