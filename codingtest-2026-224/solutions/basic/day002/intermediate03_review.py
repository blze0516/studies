import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 로직 정답 / 시간복잡도 오답
    # 시간복잡도: O(N)  — 원본 O(1) 오기재. N개 값을 한 번씩 보므로 O(N)
    # 공간복잡도: O(1)  — 배열에 모으지 않고 하나씩 확인하므로 변수만 사용
    N = int(input())
    count = 0

    for _ in range(N):
        n = int(input())
        if n > 0:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()
