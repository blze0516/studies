import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 나머지 연산과 분기만 한다.
    # 공간복잡도: O(1)  — 변수 몇 개만 사용한다.
    # 참고: 0은 짝수다. Python에서 음수도 n % 2로 판정하면 된다.
    num = int(input())

    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")


if __name__ == "__main__":
    solve()
