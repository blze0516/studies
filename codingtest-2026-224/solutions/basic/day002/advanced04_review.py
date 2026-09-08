import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 로직 정답 / 시간복잡도 오답
    # 시간복잡도: O(K)  — 원본 O(1) 오기재. 최대 K번 작업하므로 O(K)
    # 공간복잡도: O(1)  — 변수 몇 개만 사용한다.
    value, target, K = map(int, input().split())
    count = 0

    if value >= target:
        print(0)
        return

    while value < target and count < K:
        if value % 2 == 0:
            value += 3
        else:
            value += 2
        count += 1

    if value >= target:
        print(count)
    else:
        print(-1)


if __name__ == "__main__":
    solve()
