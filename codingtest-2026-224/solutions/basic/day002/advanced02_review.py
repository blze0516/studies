import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 로직 오답 / 시간복잡도 오답
    # 원인: 바로 전날이 출석인지만 봐서 3일 연속부터 점수가 2로 고정된다.
    #       1,1,1 → 원본 5점, 정답 1+2+3=6점.
    #       연속 출석 수 streak를 세고, 그날 streak만큼 더해야 한다.
    # 시간복잡도: O(N)  — 원본 O(1) 오기재. N일을 한 번씩 보므로 O(N)
    # 공간복잡도: O(1)  — 연속일수·총점 변수만 사용한다.
    N = int(input())
    streak = 0
    score = 0

    for _ in range(N):
        attend = int(input())

        if attend == 0:
            streak = 0
        else:
            streak += 1
            score += streak

    print(score)


if __name__ == "__main__":
    solve()
