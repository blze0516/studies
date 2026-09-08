import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 75 82
    # 핵심 조건: 시험 점수 score와 출석률 attendance가 주어진다.
    # 시험 점수가 70 이상
    # 출석률이 80 이상
    # 두 조건을 모두 만족하면 PASS, 아니면 FAIL을 출력하라.
    # 예상 시간복잡도: O(1)
    score, attendance = map(int, input().split())

    if score >= 70 and attendance >= 80:
        print("PASS")
    else:
        print("FAIL")

    pass


if __name__ == "__main__":
    solve()
