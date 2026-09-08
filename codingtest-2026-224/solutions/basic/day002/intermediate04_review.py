import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. N일을 한 번씩 본다.
    # 공간복잡도: O(1)  — 총점 변수만 사용한다.
    N = int(input())
    total = 0

    for _ in range(N):
        late = int(input())
        if late >= 30:
            total += 3
        elif late >= 10:
            total += 2
        elif late >= 1:
            total += 1

    print(total)


if __name__ == "__main__":
    solve()
