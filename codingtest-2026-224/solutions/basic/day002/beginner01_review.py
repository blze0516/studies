import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 비교와 출력만 한다.
    # 공간복잡도: O(1)  — 변수 몇 개만 사용한다.
    age = int(input())

    if age >= 19:
        print("ADULT")
    else:
        print("MINOR")


if __name__ == "__main__":
    solve()
