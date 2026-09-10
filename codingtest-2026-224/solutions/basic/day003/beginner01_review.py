import sys

input = sys.stdin.readline


def get_absolute(n):
    if n < 0:
        return -n
    return n


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 부호 비교와 부호 반전만 한다.
    # 공간복잡도: O(1)  — 정수 변수만 사용한다.
    n = int(input())
    print(get_absolute(n))


if __name__ == "__main__":
    solve()
