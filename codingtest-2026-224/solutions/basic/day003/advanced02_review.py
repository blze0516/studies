import sys

input = sys.stdin.readline


def calculate_fare(base, base_distance, distance, extra_fee):
    if distance <= base_distance:
        return base
    return base + (distance - base_distance) * extra_fee


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(1)  — 원본과 동일. 거리 비교와 요금 계산만 한다.
    # 공간복잡도: O(1)  — 정수 변수만 사용한다.
    base, base_distance, distance, extra_fee = map(int, input().split())
    print(calculate_fare(base, base_distance, distance, extra_fee))


if __name__ == "__main__":
    solve()
