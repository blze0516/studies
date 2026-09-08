import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 두 조건 비교만 한다.
    # 공간복잡도: O(1)  — 변수 몇 개만 사용한다.
    score, attendance = map(int, input().split())

    if score >= 70 and attendance >= 80:
        print("PASS")
    else:
        print("FAIL")


if __name__ == "__main__":
    solve()
