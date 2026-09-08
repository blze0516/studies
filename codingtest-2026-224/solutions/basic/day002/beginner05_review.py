import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 로직 정답 / 시간복잡도 오답
    # 시간복잡도: O(N)  — 원본 O(1) 오기재. 1부터 N까지 한 번씩 보므로 O(N)
    # 공간복잡도: O(1)  — 카운터 변수만 사용한다.
    num = int(input())
    count = 0

    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()
