import sys

input = sys.stdin.readline

def is_even(n):
    return n % 2 == 0

def solve() -> None:
    # 입력: 14
    # 핵심 조건: 정수 N이 주어진다. is_even(n) 함수가 짝수면 True, 홀수면 False를 반환하도록 작성하라.
    # 메인 코드에서는 반환값에 따라 EVEN 또는 ODD를 출력한다.
    # 예상 시간복잡도: O(1)
    n = int(input())

    if is_even(n):
        print("EVEN")
    else:
        print("ODD")

    pass


if __name__ == "__main__":
    solve()
