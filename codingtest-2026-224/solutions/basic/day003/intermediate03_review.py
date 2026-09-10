import sys

input = sys.stdin.readline


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 등급 구간을 정해진 횟수만 비교한다.
    # 공간복잡도: O(1)  — 점수 변수만 사용한다.
    score = int(input())
    print(get_grade(score))


if __name__ == "__main__":
    solve()
