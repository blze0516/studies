import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 조건 몇 개만 검사한다.
    # 공간복잡도: O(1)  — 변수 몇 개만 사용한다.
    # 참고: VIP와 PASS가 겹치므로 나이 → VIP → PASS 순서가 맞다.
    age, score, training = map(int, input().split())

    if age < 18:
        print("AGE_FAIL")
    elif score >= 80 and training >= 100:
        print("VIP")
    elif score >= 60 and training >= 50:
        print("PASS")
    else:
        print("FAIL")


if __name__ == "__main__":
    solve()
