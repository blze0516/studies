import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 로직 정답 / 시간복잡도 표현 부정확
    # 시간복잡도: O((target - exp) / gain)
    #   원본 O(N)은 입력에 N이 없어 부정확하다.
    #   while은 하루씩 더하므로 반복 횟수는 날 수에 비례한다.
    # 공간복잡도: O(1)  — 경험치·날 수 변수만 사용한다.
    exp, gain, target = map(int, input().split())
    days = 0

    while exp < target:
        exp += gain
        days += 1

    print(days)


if __name__ == "__main__":
    solve()
