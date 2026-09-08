import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 로직 정답 / 시간복잡도 오답
    # 시간복잡도: O(N)  — 원본 O(1) 오기재. 1부터 N까지 한 번씩 보므로 O(N)
    # 공간복잡도: O(1)  — 총점 변수만 사용한다.
    # 참고: 한 숫자가 여러 배수를 만족하면 점수를 모두 더하므로 if 세 개가 맞다.
    N = int(input())
    score = 0

    for i in range(1, N + 1):
        if i % 2 == 0:
            score += 1
        if i % 3 == 0:
            score += 2
        if i % 5 == 0:
            score += 3

    print(score)


if __name__ == "__main__":
    solve()
