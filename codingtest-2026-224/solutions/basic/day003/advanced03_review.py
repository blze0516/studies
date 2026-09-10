import sys

input = sys.stdin.readline


def get_max_score(scores):
    max_score = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
    return max_score


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 점수 N개를 한 번씩 본다.
    # 공간복잡도: O(N)  — 점수 리스트를 저장한다.
    n = int(input())
    scores = list(map(int, input().split()))
    print(get_max_score(scores))


if __name__ == "__main__":
    solve()
